from loader import image_loader, get_device
import torch
import torch.optim as optim
import torchvision.models as models
from model import get_style_model_and_losses
import conf as configs
import numpy as np

from writer import write_image

device = get_device()
print("device", device)

def get_input_optimizer(conf, input_img):
    # this line to show that input is a parameter that requires a gradient
    if conf.optimizer == 'Adam':
        return optim.Adam([input_img], lr=0.2)
    else:
        return optim.LBFGS([input_img], lr=0.2)




def run_conf(conf):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    style_img = image_loader(device, conf.style_image_path)
    content_img = image_loader(device, conf.content_image_path)
    assert style_img.size() == content_img.size(), \
        "we need to import style and content images of the same size"

    cnn = models.vgg19(pretrained=True).features.to(device).eval()
    cnn_normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
    cnn_normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(device)

    # Initialize with a bit of noise
    ###input_img = content_img.clone().to(device)
    input_img = torch.tensor(np.random.random(size=content_img.shape), dtype=torch.float).to(device)



    model, style_losses, content_losses = \
        get_style_model_and_losses(
            device,
            cnn,
            cnn_normalization_mean,
            cnn_normalization_std,
            style_img,
            content_img,
            conf.content_layers,
            conf.style_layers)

    # We want to optimize the input and not the model parameters so we
    # update all the requires_grad fields accordingly
    input_img.requires_grad_(True)
    model.requires_grad_(False)

    optimizer = get_input_optimizer(conf, input_img)

    def closure():
        # correct the values of updated input image
        with torch.no_grad():
            input_img.clamp_(0, 1)

        optimizer.zero_grad()
        model(input_img)

        style_score = sum([a.loss for a in style_losses])
        content_score = sum([a.loss for a in content_losses])

        style_score *= conf.style_weight
        content_score *= conf.content_weight

        loss = style_score + content_score
        loss.backward()

        return loss

    last_total_loss=1e10
    for istep in range(conf.numiter):

        total_loss=optimizer.step(closure)
        style_score = sum([a.loss for a in style_losses]) * conf.style_weight
        content_score = sum([a.loss for a in content_losses]) * conf.content_weight
        print(f"style:{style_score} content:{content_score}")
        print(f'total loss: {total_loss}')

        if istep % conf.writeevery == 0:
            write_image(input_img, f"{conf.output_image_name}", f"step_{istep}")

        for g in optimizer.param_groups:
            g['lr'] = g['lr'] * 0.97

        # # Adaptive learning rate
        # if istep % conf.reduceevery == 0:
        #     # decrease learning rate if the loss increases
        #     if total_loss>last_total_loss*0.95:
        #         for g in optimizer.param_groups:
        #             g['lr'] =  g['lr']*0.2
        #             print("Reduced learning rate")
        #     # # Increase learning rate if the loss drops very slowly
        #     # if total_loss<last_total_loss and total_loss>last_total_loss*0.99:
        #     #     for g in optimizer.param_groups:
        #     #         g['lr'] = g['lr'] * 2.0
        #     #         print("Increased learning rate")
        #     last_total_loss=total_loss

    # a last correction...
    with torch.no_grad():
        input_img.clamp_(0, 1)

    write_image(input_img, f"{conf.output_image_name}", f"final")


generated_configs = configs.config_gen(
        content_image_path="./data/images/content/edritz_1200x800.jpg",
        style_image_path="./data/images/neural-style/pencil_1200x800.jpg",
        output_image_name="edritz_pencil")

for conf in generated_configs:
    run_conf(conf)



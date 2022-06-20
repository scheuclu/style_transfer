from loader import image_loader, get_device
import torch
import torch.optim as optim
import torchvision.models as models
from model import get_style_model_and_losses
from utils import imshow, imwrite
from conf import standard_configs
import numpy as np

device = get_device()
conf = standard_configs[0]

def get_input_optimizer(conf, input_img):
    # this line to show that input is a parameter that requires a gradient
    #optimizer =
    if conf.optimizer == 'Adam':
        return optim.Adam([input_img])
    else:
        return optim.LBFGS([input_img])


def run_conf(conf):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    style_img = image_loader(device, conf.style_image_path)
    content_img = image_loader(device, conf.content_image_path)
    assert style_img.size() == content_img.size(), \
        "we need to import style and content images of the same size"
    imwrite(style_img, name=f"{conf.output_image_name}_style")
    imwrite(content_img, name=f"{conf.output_image_name}_content")

    cnn = models.vgg19(pretrained=True).features.to(device).eval()
    cnn_normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
    cnn_normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(device)

    input_img = content_img.clone()
    # input_img = content_img.clone()+torch.Tensor(np.random.random(size=content_img.shape)).to(device)*0.1
    # input_img=input_img/input_img.max()


    model, style_losses, content_losses = \
        get_style_model_and_losses(
            device,
            cnn,
            cnn_normalization_mean,
            cnn_normalization_std,
            style_img,
            content_img)

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

        return style_score + content_score

    for istep in range(conf.numiter):

        total_loss=optimizer.step(closure)
        style_score = sum([a.loss for a in style_losses]) * conf.style_weight
        content_score = sum([a.loss for a in content_losses]) * conf.content_weight
        print(f"style:{style_score} content:{content_score}")
        print(f'total loss: {total_loss}')

        if istep % conf.writeevery == 0:
            imwrite(input_img, name=f"{conf.output_image_name}_step{istep}")

    # a last correction...
    with torch.no_grad():
        input_img.clamp_(0, 1)

    print(input_img)


run_conf(standard_configs[0])


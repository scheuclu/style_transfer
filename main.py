from loader import image_loader
import torch
import torch.optim as optim
import torchvision.models as models
from model import get_style_model_and_losses
from utils import imshow, imwrite
from conf import standard_configs
import numpy as np


conf = standard_configs[0]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
style_img = image_loader(conf.style_image_path)
content_img = image_loader(conf.content_image_path)
assert style_img.size() == content_img.size(), \
    "we need to import style and content images of the same size"
imwrite(style_img, name=f"{conf.output_image_name}_style")
imwrite(content_img, name=f"{conf.output_image_name}_content")




cnn = models.vgg19(pretrained=True).features.to(device).eval()
cnn_normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
cnn_normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(device)


input_img = content_img.clone()

input_img = content_img.clone()+torch.Tensor(np.random.random(size=content_img.shape))*0.1
input_img=input_img/input_img.max()

#imwrite(input_img, name=f"{conf.output_image_name}_0")



def get_input_optimizer(input_img):
    # this line to show that input is a parameter that requires a gradient
    optimizer = optim.LBFGS([input_img])
    #optimizer = optim.Adam([input_img])
    return optimizer

# def run_style_transfer(cnn, normalization_mean, normalization_std,
#                        content_img, style_img, input_img, num_steps=50,
#                        style_weight=1000000, content_weight=1):
"""Run the style transfer."""
print('Building the style transfer model..')
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

optimizer = get_input_optimizer(input_img)

print('Optimizing..')



def style_score():
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

    return style_score+content_score

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

    return style_score+content_score

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



imshow(input_img, title='Output Image')

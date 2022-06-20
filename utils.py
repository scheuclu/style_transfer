import matplotlib.pyplot as plt


import torchvision.transforms as transforms
from torchvision.utils import save_image
import os

unloader = transforms.ToPILImage()  # reconvert into PIL image

def imshow(tensor, title=None):
    image = tensor.cpu().clone()  # we clone the tensor to not do changes on it
    image = image.squeeze(0)  # remove the fake batch dimension
    image = unloader(image)
    plt.figure()
    plt.imshow(image)
    if title is not None:
        plt.title(title)
    #plt.pause(0.001)  # pause a bit so that plots are updated



def imwrite(tensor, name, path="./output"):
    outpath=os.path.join(path,name)+".jpg"
    save_image(tensor, outpath)
    print(f"Wrote image to {outpath}")
    pass
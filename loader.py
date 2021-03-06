from PIL import Image
import torchvision.transforms as transforms
import torch

def get_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("device", device)

imsize = 800

def image_loader(device, image_name):
    loader = transforms.Compose([
        transforms.Resize(imsize),  # scale imported image
        transforms.ToTensor()])  # transform it into a torch tensor
    image = Image.open(image_name)
    image = loader(image).unsqueeze(0)
    return image.to(device, torch.float)
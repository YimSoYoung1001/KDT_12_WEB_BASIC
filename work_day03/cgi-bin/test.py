from PIL import Image
import torchvision.transforms as transforms
import torch


img = Image.open('../img/240411_200157_aaa.jpg')


preprocessing = transforms.Compose([
    transforms.Resize(size = (150, 150)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])
p_img = preprocessing(img)
print(p_img.shape)

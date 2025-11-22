import os
import cv2
import random
import numpy as np

def uint2single(img):
    return np.float32(img/255.)

def single2uint(img):
    return np.uint8((img.clip(0, 1)*255.).round())

psnr = 20
noise_path = r'/data/yangfan/pytorch/MPI/image_processing/data/noise'
# img_path = r'/data/yangfan/MPI/image_processing/deblur/KAIR-self/dataset/exam5_mnist_9T/train/train_L'
img_path = r'/data/yangfan/pytorch/MPI/image_processing/data/fangti/fangti/6T'

noise_list = os.listdir(noise_path)
img_list = os.listdir(img_path)
# out_path = rf'/data/yangfan/MPI/image_processing/deblur/KAIR-self/dataset/exam5_mnist_9T/train/train_L_noise'
out_path = rf'/data/yangfan/pytorch/MPI/image_processing/data/fangti/fangti/noisy'

patch_size = 120

if not os.path.exists(out_path):
    os.makedirs(out_path)

for img_name in img_list:
    img = cv2.imread(os.path.join(img_path,img_name),0)
    ns_idx = random.randint(0,len(noise_list)-1)
    noise_name = noise_list[ns_idx]
    noise = cv2.imread(os.path.join(noise_path,noise_name),0)
    H, W = noise.shape
    rnd_h = random.randint(0, max(0, H - patch_size))
    rnd_w = random.randint(0, max(0, W - patch_size))
    noise = noise[rnd_h:rnd_h + patch_size, rnd_w:rnd_w + patch_size]
    psnr = random.uniform(15,20)
    sigma = 255. / (noise.sum() / (patch_size ** 2) * np.sqrt(10 ** (psnr / 10)))

    img = uint2single(img)
    noise = uint2single(noise)
    img_noise = img + sigma * noise
    cv2.imwrite(os.path.join(out_path,img_name),single2uint(img_noise))


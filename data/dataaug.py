import os
import cv2
import numpy as np
import random

def find_files_with_extension(root_folder, target_extension):
    file_paths = []

    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith(target_extension):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    return file_paths

def random_flip(image):
    flip_code = random.randint(-1, 1)
    return cv2.flip(image, flip_code)

def random_rotate(image):
    angle = random.randint(0, 360)
    rows, cols = image.shape
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    return cv2.warpAffine(image, M, (cols, rows))

def random_brightness(image):
    alpha = random.uniform(0.6, 1.0)
    # beta = random.uniform(0, 1.0)
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

def random_resize_and_pad(image):
    # 随机选择缩放比例
    scale_factor = random.uniform(0.6, 1.0)

    # 缩放图像
    resized_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

    # 获取原始图像和缩放后图像的尺寸
    h, w = image.shape[:2]
    new_h, new_w = resized_image.shape[:2]

    # 计算padding的尺寸
    top = (h - new_h) // 2
    bottom = h - new_h - top
    left = (w - new_w) // 2
    right = w - new_w - left

    # 对缩放后的图像进行padding
    padded_image = cv2.copyMakeBorder(resized_image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0)

    return padded_image

def apply_random_augmentations(image):
    image = random_flip(image)
    image = random_rotate(image)
    # image = random_resize_and_pad(image)
    # image = random_brightness(image)
    return image


root_path = r'/data/yangfan/pytorch/MPI/image_processing/data/fangti/gray/train_test_split'
target_extension = '.png'  # 指定需要查找的后缀，如'.txt', '.csv', '.jpg'等
output_path = r'/data/yangfan/pytorch/MPI/image_processing/data/fangti/gray/train_test_split/augmentation'
os.makedirs(output_path, exist_ok=True)
num_augmentations = 7
# 获取符合条件的文件路径列表
file_list = find_files_with_extension(root_path, target_extension)

for file_path in file_list:
    _, name = os.path.split(file_path)
    gray_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    save_path = os.path.join(output_path, name.replace('.png',f'_aug_0.png'))
    cv2.imwrite(save_path, gray_image)
    for i in range(num_augmentations):
        augmented_image = apply_random_augmentations(gray_image)
        save_path = os.path.join(output_path, name.replace('.png',f'_aug_{i+1}.png'))
        cv2.imwrite(save_path, augmented_image)


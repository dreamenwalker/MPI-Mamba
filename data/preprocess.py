from PIL import Image
import random
import multiprocessing as mp
import random
import numpy as np
import os

img_path = r'E:\杨帆\研究生\科研\data\deblur\all_data\MNIST'
num = 4000
out_path = r'E:\杨帆\研究生\科研\data\deblur\dataset2_mnist\origin'
os.makedirs(out_path, exist_ok=True)
img_size = (120,120)
def preprocess(path):
    img = Image.open(path)
    scale = 1.0
    # img_name = 'mnist_' + os.path.split(path)[1].split('.')[0] + '_6T.png'
    img_name = f'mnist_' + os.path.split(path)[1].split('.')[0] + '.png'
    resized_img = img.resize(img_size)
    # resized_img_arr = (np.array(resized_img) * random.uniform(0.5, 1)).astype(np.uint8)
    # resized_img_arr = (np.array(resized_img) * scale).astype(np.uint8)
    # processed_image = Image.fromarray(resized_img_arr)
    resized_img.save(os.path.join(out_path,img_name))


if __name__ == '__main__':
    img_path_list = os.listdir(img_path)
    index = list(range(len(img_path_list)))
    random.shuffle(index)
    # index_ch = index[:num]
    index_ch = index
    img_path_ch_list = [img_path_list[i] for i in index_ch]
    pool = mp.Pool()
    pool.map(preprocess,[os.path.join(img_path,f) for f in img_path_ch_list])

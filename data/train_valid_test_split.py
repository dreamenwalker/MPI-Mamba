import numpy as np
import shutil
import os


input_path = r'/data/yangfan/pytorch/MPI/image_processing/data/fangti/fangti/gt'
out_path = r'/data/yangfan/pytorch/MPI/image_processing/deblur/dataset/fangti'
type_list = ['train','valid','test']
quality = 'H'

for type in type_list:
    input_list = [f for f in os.listdir(input_path) if type in f]
    for name in input_list:
        origin_path = os.path.join(input_path,name)
        out_folder_path = os.path.join(out_path, type, type + '_' + quality)
        os.makedirs(out_folder_path,exist_ok=True)
        save_path = os.path.join(out_folder_path, name)
        shutil.copy2(origin_path, save_path)
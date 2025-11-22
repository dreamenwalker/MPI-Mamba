import os
import shutil

def find_files_with_extension(root_folder, target_extension):
    file_paths = []

    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith(target_extension):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    return file_paths



# 指定根文件夹和目标后缀
root_folder_path = '/data/yangfan/pytorch/MPI/image_processing/data/fangti/gray'
target_path = '/data/yangfan/pytorch/MPI/image_processing/data/fangti/gray/All'
target_extension = '.png'  # 指定需要查找的后缀，如'.txt', '.csv', '.jpg'等

# 获取符合条件的文件路径列表
file_paths = find_files_with_extension(root_folder_path, target_extension)
os.makedirs(target_path,exist_ok=True)
for file in file_paths:
    file_name = os.path.split(file)[1]
    file_out_path = os.path.join(target_path,file_name)
    shutil.copy(file,file_out_path)
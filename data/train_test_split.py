import os
import random
import shutil
random.seed(0)

data_path = r'/data_raid5_21T/yangfan/pytorch/MPI/image_processing/data/dataset4_vessel/gt'
train_path = r'/data_raid5_21T/yangfan/pytorch/MPI/image_processing/deblur/dataset/vessel/train/train_H'
test_path = r'/data_raid5_21T/yangfan/pytorch/MPI/image_processing/deblur/dataset/vessel/test/test_H'

if not os.path.exists(train_path):
    os.makedirs(train_path)

if not os.path.exists(test_path):
    os.makedirs(test_path)

data = sorted([f for f in os.listdir(data_path) if f.startswith(('mnist','vessel'))])
random.shuffle(data)
num = 6470
train_data, test_data = data[:num], data[num:]
for name in train_data:
    origin_path = os.path.join(data_path,name)
    save_path = os.path.join(train_path,name)
    shutil.copy2(origin_path,save_path)

for name in test_data:
    origin_path = os.path.join(data_path,name)
    save_path = os.path.join(test_path,name)
    shutil.copy2(origin_path,save_path)


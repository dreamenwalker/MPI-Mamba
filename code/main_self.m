close all;
clc;
clear all;

file_path = './data-hanzi/';
file_result_path = './result5/';

% 匹配.jpg、.png、.jpeg文件
img_path_list_jpg = dir(strcat(file_path, '*.jpg'));
img_path_list_png = dir(strcat(file_path, '*.png'));
img_path_list_jpeg = dir(strcat(file_path, '*.jpeg'));

% 合并三种类型的图像文件列表
img_path_list = [img_path_list_jpg; img_path_list_png; img_path_list_jpeg];

img_num = length(img_path_list);
fprintf('正在读取的图像为：\n');
if img_num > 0 
    for j = 1:img_num 
        image_name = img_path_list(j).name;
        img = strcat(file_path, image_name);
        fprintf('第%d个：%s\n', j, img);  % 显示正在处理的图像名
        %result = xspace(img);
        result = flipud(xspace(img));
        % 分割文件名和扩展名
        [filepath, name, ext] = fileparts(image_name);
        
        % 在文件名后添加编号
        new_image_name = strcat(name, '_', ext);
        
        % 保存结果图像
        imwrite(result, strcat(file_result_path, new_image_name));
    end
end

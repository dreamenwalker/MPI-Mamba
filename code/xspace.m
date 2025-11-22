G = 9;
path = '/data/yangfan/pytorch/MPI/image_processing/data/fangti/fangti_test/gray/origin';
gt_path = '/data/yangfan/pytorch/MPI/image_processing/data/fangti/fangti_test/gray/9T/gt';
out_path = '/data/yangfan/pytorch/MPI/image_processing/data/fangti/fangti_test/gray/9T/9T';
decv_path = '/data/yangfan/pytorch/MPI/image_processing/data/fangti/fangti_test/gray/9T/deconv';

dir_result = dir(path);
filenames = {dir_result.name};  % 将所有文件名存储在一个字符串数组�?
filenames = filenames(~ismember(filenames,{'.','..'}));  % 去除 "." �?".." 文件�?
file_paths = fullfile(path,filenames);
[dot_blur] = x_space_dot(G);
rng(0);
c0_list = 0.4 * rand(1,length(file_paths)) + 0.6;
tic
parfor i=1:length(file_paths)
%    c0 = c0_list(i);
    c0 = 1
    [img_gt, img_blur] = x_space(file_paths{i},c0,G);
    img_decv = deconvlucy(img_blur, dot_blur, 20);
%    img_decv = deconvwnr(img_blur, dot_blur,0,fftshift(real(ifft2(abs(fft2(img_blur)).^2))));
    img_parl_decv = c0 * img_decv/max(img_decv(:));
    [~, name, ext] = fileparts(file_paths{i});
    filename = strcat(name,ext);
    gt_save_path = fullfile(gt_path,filename);
    out_save_path = fullfile(out_path,filename);
    decv_save_path = fullfile(decv_path,filename);
    imwrite(img_gt, gt_save_path);
    imwrite(img_blur, out_save_path);
    imwrite(img_parl_decv, decv_save_path);
end
run_time = toc;
%disp(['runtime: ' num2str(toc)]);

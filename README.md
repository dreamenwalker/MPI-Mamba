## MPI-Mamba

中文简介
- MPI-Mamba 面向磁粒子成像（MPI）中的各向异性校准与去模糊任务，采用基于 Mamba 的潜特征融合与层级结构以获得高效的重建效果。

English Overview
- MPI-Mamba targets anisotropic calibration and deblurring in Magnetic Particle Imaging (MPI), leveraging a Mamba-based latent feature fusion with a hierarchical encoder–decoder for efficient restoration.

## Installation | 安装
- Python `3.9`
- PyTorch `>=1.9.0`
- NVIDIA GPU + [CUDA](https://developer.nvidia.com/cuda-downloads)

```bash
cd mpi-mamba
conda create -n mpi-mamba python=3.9
conda activate mpi-mamba
pip install -r requirements.txt
```

## Datasets | 数据集
- 训练/验证使用成对数据：`GT` 为目标高清图像，`LQ` 为对应的低质量/含噪图像。
- 在配置文件中使用占位符来指示路径用途（见下文“配置含义”）。

## Training | 训练
- Stage-1（示例）：

```bash
python train.py -opt options/train/Realdata_S1.yml
```

- Stage-2（示例）：

```bash
python train.py -opt options/train/Realdata_S2.yml
```

- 训练日志与模型保存在 `experiments/` 目录。

## Testing | 测试
- 使用示例配置：

```bash
python test.py -opt options/test/test.yml
```

- 测试结果保存在 `results/` 目录。

## Option Semantics | 配置含义
- 请根据本地数据与模型文件替换为真实路径。
- 常见字段含义：
  - `datasets.train.dataroot_gt`: 训练集 GT（高清/标注）图像所在目录。
  - `datasets.train.dataroot_lq`: 训练集 LQ（低质量/含噪）图像所在目录。
  - `datasets.val.*.dataroot_gt`: 验证集 GT 图像目录。
  - `datasets.val.*.dataroot_lq`: 验证集 LQ 图像目录。
  - `path.pretrain_network_g`: 生成器的预训练权重文件路径。
  - `path.pretrain_network_le`: 潜编码器（Stage-1）的预训练权重文件路径。
  - `path.pretrain_network_le_dm`: 潜编码器（Stage-2/去噪模块）的预训练权重文件路径。
  - `path.pretrain_network_d`: 去噪网络的预训练权重文件路径。
  - `path.resume_state`: 断点恢复的训练状态文件路径。

## Citation | 引用
If you find the code helpful in your research or work, please cite:

```
@inproceedings{zhang2026mpimamba,
  title={MPI-Mamba: Latent Feature Fusion Mamba for Anisotropic Image Calibration and Deblurring in Magnetic Particle Imaging},
  author={Zhang, Liwen and Miao, Zhaoji and Shen, Yusong and Wei, Zechen and Hui, Hui and Jie, Tian},
  booktitle={AAAI},
  year={2026}
}
```

## Acknowledgements | 致谢
This code builds upon:
- BasicSR: https://github.com/XPixelGroup/BasicSR
- Restormer: https://github.com/swz30/Restormer
- HI-Diff: https://github.com/zhengchen1999/HI-Diff
- DiffIR: https://github.com/Zj-BinXia/DiffIR

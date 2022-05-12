# AlphaRotate: A Rotation Detection Benchmark using TensorFlow 1.13.1 -> 2.2.0

[![Documentation Status](https://readthedocs.org/projects/rotationdetection/badge/?version=latest)](https://rotationdetection.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://badge.fury.io/py/alpharotate.svg)](https://badge.fury.io/py/alpharotate)
[![Downloads](https://pepy.tech/badge/alpharotate)](https://pepy.tech/project/alpharotate)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Average time to resolve an issue](https://isitmaintained.com/badge/resolution/yangxue0827/RotationDetection.svg)](https://github.com/yangxue0827/RotationDetection/issues)
[![Percentage of issues still open](https://isitmaintained.com/badge/open/yangxue0827/RotationDetection.svg)](https://github.com/yangxue0827/RotationDetection/issues)

<!-- Documentation: [https://rotationdetection.readthedocs.io/](https://rotationdetection.readthedocs.io/) -->

 <!-- :rocket::rocket::rocket:	**News:** The MMDetection version cooperating with MMLab will be released soon, stay tuned.:rocket::rocket::rocket: -->
 :rocket::rocket::rocket:	**News:** MMRotate has been released at https://github.com/open-mmlab/mmrotate <img src="https://img.shields.io/github/stars/open-mmlab/mmrotate?style=social" /> :rocket::rocket::rocket:

| Method | Baseline |    DOTA1.0  |   DOTA1.5   |   DOTA2.0   | Model | Anchor | Angle Pred. | Reg. Loss| Angle Range | Configs |      
|:------------:|:------------:|:-----------:|:----------:|:-----------:|:----------:|:-----------:|:-----------:|:-----------:|:---------:|:---------:|    
| [KFIoU](https://arxiv.org/abs/2201.12558) | [R<sup>3</sup>Det](https://arxiv.org/abs/1908.05612) | 72.28 | 64.69 | 50.41 | [Baidu Drive (u77v)](https://pan.baidu.com/s/1n5eqqqE0j3dhYgXM-4_k5A) | H->R | Reg. (∆⍬) | **kfiou** | [-90,0)  | [dota1.0,](./configs/DOTA/r3det_kfiou/cfgs_res50_dota_r3det_kf_v5.py) [dota1.5,](./configs/DOTA1.5/r3det_kfiou/cfgs_res50_dota1.5_r3det_kf_v4.py) [dota2.0](./configs/DOTA2.0/r3det_kfiou/cfgs_res50_dota2.0_r3det_kf_v4.py) |

## Installation
### Manual configuration (cuda version < 11)
```shell
# 가상환경 먼저 만든 후 (python=3.6)
pip install cython
pip install numpy
# 원래는 pip install -r -e . 를 해야하지만 이렇게하면 
# tensorflow 1.13.1관련된게 엄청 깔리니까 이렇게 하지말고
conda install tensorflow==2.2.0
conda install -c anaconda tensorflow-gpu==2.2.0 # 이거 해야 GPU 쓰는듯
## conda list로 tensorflow잘 설치되어있나 확인

# 설치해 주어야함
conda install -c conda-forge tf_slim
conda install -c conda-forge opencv
conda install -c anaconda pillow
conda install -c conda-forge tqdm
```

## Download Model
### Pretrain weights put them to => $PATH_ROOT/dataloader/pretrained_weights. 
1. MxNet pretrain weights **(recommend in this repo, default in [NET_NAME](./configs/_base_/models/retinanet_r50_fpn.py))**: resnet_v1d, resnet_v1b, refer to [gluon2TF](./thirdparty/gluon2TF/README.md).    
* [Baidu Drive (5ht9)](https://pan.baidu.com/s/1GpqKg0dOaaWmwshvv1qWGg)          
* [Google Drive](https://drive.google.com/drive/folders/1BM8ffn1WnsRRb5RcuAcyJAHX8NS2M1Gz?usp=sharing)  
2. Tensorflow pretrain weights: [resnet50_v1](http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz)
3. Pytorch pretrain weights, refer to [pretrain_zoo.py](./dataloader/pretrained_weights/pretrain_zoo.py) and [Others](./OTHERS.md).
* [Google Drive](https://drive.google.com/drive/folders/14Bx6TK4LVadTtzNFTQj293cKYk_5IurH?usp=sharing)      

### Trained weights put them to => $PATH_ROOT/output/trained_weights.

### Visualization is in => $PATH_ROOT/tools/r3det_kfiou/test_dota/VERSION

## Test
    ```  
    python test_dota_sota.py --test_dir='/PATH/TO/IMAGES/'  
                             --gpus=0,1,2,3,4,5,6,7  
                             -s (visualization, optional)
                             -cn (use cpu nms, slightly better <1% than gpu nms but slower, optional)
    ``` 


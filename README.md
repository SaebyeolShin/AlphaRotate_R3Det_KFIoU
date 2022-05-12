# AlphaRotate : R3Det_KFIoU 1.13.1 -> 2.2.0

## Installation
```shell
# 가상환경 먼저 만든 후 (python=3.6)
pip install cython
pip install numpy

# 원래는 pip install -r -e . 를 해야하지만 이렇게하면 
# tensorflow 1.13.1관련된게 엄청 깔리니까 이렇게 하지말고
conda install tensorflow==2.2.0
conda install -c anaconda tensorflow-gpu==2.2.0 # 이거 해야 GPU 씀
## conda list로 tensorflow잘 설치되어있나 확인

# 설치해 주어야함
conda install -c conda-forge tf_slim
conda install -c conda-forge opencv
conda install -c anaconda pillow
conda install -c conda-forge tqdm
```

## Download Model
### 1. Pretrain weights put them to => $PATH_ROOT/dataloader/pretrained_weights. 
+ [MxNet pretrain weights](https://drive.google.com/drive/folders/1BM8ffn1WnsRRb5RcuAcyJAHX8NS2M1Gz?usp=sharing) (resnet50v1d.ckpt~ 만 다운)
+ [Tensorflow pretrain weights: resnet50_v1](http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz)
+ [Pytorch pretrain weights](https://drive.google.com/drive/folders/14Bx6TK4LVadTtzNFTQj293cKYk_5IurH?usp=sharing) (resnet50.npy 만 다운)

### 2. [Trained weights](https://pan.baidu.com/s/1n5eqqqE0j3dhYgXM-4_k5A) put them to => $PATH_ROOT/output/trained_weights.

### 3. Visualization is in => $PATH_ROOT/tools/r3det_kfiou/test_dota/VERSION

## Test
```shell
# large-scale image, take DOTA dataset as a example
python test_dota_sota.py --test_dir='/PATH/TO/IMAGES/'  
                         --gpus=0,1,2,3,4,5,6,7  
                         -s (visualization, optional)
                         -cn (use cpu nms, slightly better <1% than gpu nms but slower, optional)

# small-scale image, take HRSC2016 as a example
python test_hrsc2016.py --img_dir='/PATH/TO/IMAGES/'  
                        --gpu=0
                        -s (visualization, optional)
``` 


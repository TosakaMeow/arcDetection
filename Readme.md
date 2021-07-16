## 基于STFT与DNN的电流异常检测

### 一、开发环境
    OS：Windows 11 Pro for Workstations
    Python版本：3.7
    CUDA版本：10.2、11.0
    TensorFlow版本：2.4.2
    Keras版本：2.4.3

### 二、文件介绍
### （1）train.py
    用于构建、训练神经网络的文件。
### （2）pretreat.py
    主要用于对数据进行预处理，将原始的时间序列数据转换为具有23个特征的
    新数据集作为训练集和测试集。
### （4）predict.py
    这个文件主要进行验证集或者新数据集的预测。
### （5）其他文件
    data_train.csv为训练集
    data_test.csv为测试集
    *.h5为保存的神经网络模型
    kwargs.py保存了整个项目的参数
    ......
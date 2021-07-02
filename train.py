import pandas as pd
import numpy as np
import keras
from keras import layers
import matplotlib.pyplot as plt
import kwargs
from sklearn.utils import shuffle


def train_main(path):
    # 读取训练集
    data = pd.read_csv(path)
    # 打乱数据
    data = shuffle(data)
    # 提取数据集前九列作为输入
    data_train = data[["f1", "f2", "f3", "f4",
                       "f5", "f6", "f7", "f8", "f9",
                       "f10", "f11", "f12", "f13", "f14",
                       "f15", "f16", "f17", "f18", "f19"]]

    # 提取数据集第十列并reshape作为标签
    data_target = data["label"].values.reshape(len(data), 1)
    print(np.shape(data_train), np.shape(data_target))

    # 构建模型
    model = keras.Sequential()
    # model.add(layers.Dense(32, input_dim=10, activation="softmax"))
    model.add(layers.Dense(16, activation='relu', input_shape=(19,)))
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    # 编译模型
    model.compile(optimizer="adam",
                  loss="binary_crossentropy",
                  metrics=["acc"]
                  )

    # 训练模型
    history = model.fit(data_train, data_target, epochs=kwargs.DNN.epochs, batch_size=64)

    # 保存模型
    model.save("model.h5")

    # 绘制训练精度图
    plt.plot(range(kwargs.DNN.epochs), history.history.get('acc'))
    plt.xlabel("epochs")
    plt.ylabel("accuracy")
    plt.show()

train_main("data_train.csv")
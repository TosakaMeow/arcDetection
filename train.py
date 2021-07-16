'''
 * Copyright@violetnris@outlook.com
 * Author:王昊
 * Date:2021.07.16
 '''

import keras
import keras.layers
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Model
from sklearn.utils import shuffle
import kwargs


def train_main(path):
    # 读取训练集
    train_data = pd.read_csv("./data_train_ver3.0.csv")

    # 打乱数据
    data = shuffle(train_data)

    data = data[int(len(data) *0.2):]
    conv_x = data[["area", "low", "high"]].values.reshape(len(data), 1, 3)
    conv_y = data["label"].values.reshape(len(data), 1, 1)
    base_x = data[["f1", "f2", "f3", "f4", "f5",
                   "f6", "f7", "f8", "f9", "f10",
                   "f11","f12", "f13", "f14", "f15",
                   "f16","f17", "f18", "f19", "f20"]].values.reshape(len(data), 1, 20)
    base_y = data["label"].values.reshape(len(data), 1)

    # 打乱数据
    evaluate_data = data[:int(len(data) *0.2)]
    evaluate_conv_x = evaluate_data[["area", "low", "high"]].values.reshape(len(evaluate_data), 1, 3)
    evaluate_conv_y = evaluate_data["label"].values.reshape(len(evaluate_data), 1, 1)
    evaluate_base_x = evaluate_data[["f1", "f2", "f3", "f4", "f5",
                                     "f6", "f7", "f8", "f9", "f10",
                                     "f11","f12", "f13", "f14", "f15",
                                     "f16","f17", "f18", "f19", "f20"]].values.reshape(len(evaluate_data), 1, 20)
    evaluate_base_y = evaluate_data["label"].values.reshape(len(evaluate_data), 1)

    # 对连续数据进行拟合
    conv_model = keras.Sequential()
    conv_model.add(layer=keras.layers.Dense(32, activation='relu', input_shape=(None, 3)))
    conv_model.add(
        layer=keras.layers.Conv1D(filters=6, kernel_size=100, strides=10, padding='same'))
    conv_model.add(layer=keras.layers.MaxPooling1D(pool_size=6, strides=2, data_format='channels_first'))
    conv_model.add(layer=keras.layers.Dropout(0.5))
    conv_model.add(layer=keras.layers.Dense(32, activation='relu'))
    conv_model.add(layer=keras.layers.Dropout(0.5))
    conv_model.add(layer=keras.layers.Dense(16))
    conv_input = conv_model.input
    conv_output = conv_model.output
    # 对离散数据进行拟合
    base_model = keras.Sequential()
    base_model.add(layer=keras.layers.Dense(32, activation='relu', input_shape=(None, 20)))
    base_model.add(layer=keras.layers.Dropout(0.5))
    base_model.add(layer=keras.layers.Dense(32, activation='relu'))
    base_model.add(layer=keras.layers.Dropout(0.5))
    base_model.add(layer=keras.layers.Dense(16))
    base_input = base_model.input
    base_output = base_model.output
    # 模型融合
    concatenated = keras.layers.concatenate([base_output, conv_output])
    model = keras.layers.Dense(32, activation="relu")(concatenated)
    model = keras.layers.Dense(32, activation="relu")(model)
    model_output = keras.layers.Dense(1, activation="sigmoid")(model)
    model = Model(inputs=[base_input, conv_input], outputs = model_output)
    # 编译模型
    model.compile(optimizer="adam",
                       loss="binary_crossentropy",
                       metrics=["acc"]
                       )

    # 训练模型
    history = model.fit([base_x, conv_x], conv_y, epochs=kwargs.DNN.epochs, batch_size=16)
    print("正在进行验证......")
    loss, accuracy = model.evaluate([evaluate_base_x, evaluate_conv_x], evaluate_conv_y, batch_size=16)
    print("验证集的准确率为：",accuracy)




    # 保存模型
    model.save(kwargs.DNN.test_model)

    # 绘制训练精度图
    plt.plot(range(kwargs.DNN.epochs), history.history.get('acc'))
    plt.xlabel("epochs")
    plt.ylabel("accuracy")
    plt.show()


train_main("D:/DataSource/")

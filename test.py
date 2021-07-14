import pandas as pd
import numpy as np
import keras
from keras.models import Sequential
import keras.layers
import matplotlib.pyplot as plt
import kwargs
from sklearn.utils import shuffle

train_data = pd.read_csv("./data_train_ver3.0.csv")
evaluate_data = pd.read_csv("./data_evaluate_ver3.0.csv")
# 打乱数据
data = shuffle(train_data.append(evaluate_data))

data = data[:len(data) *0.2]
conv_x = data[["area"]].values.reshape(len(data), 1, 1)
conv_y = data["label"].values.reshape(len(data), 1, 1)
base_x = data[["low", "high"]].values.reshape(len(data), 1, 2)
base_y = data["label"].values.reshape(len(data), 1)
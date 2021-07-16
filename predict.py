'''
 * Copyright@violetnris@outlook.com
 * Author:王昊
 * Date:2021.07.16
 '''
import pandas as pd
from sklearn.utils import shuffle
import xlwt
from keras.models import load_model
import kwargs

wb = xlwt.Workbook()
sh = wb.add_sheet('1')

model = load_model(kwargs.DNN.test_model)
print("模型加载完毕！")

print("正在进行准备测试......")
test_data = pd.read_csv("./data_evaluate_ver3.0.csv")
data = shuffle(test_data)
conv_x = data[["area"]].values.reshape(len(data), 1, 1)
conv_y = data["label"].values.reshape(len(data), 1, 1)
base_x = data[["low", "high", "f2", "f3", "f4",
                    "f5", "f6", "f7", "f8", "f9", "f10",
                    "f12", "f13", "f14", "f15", "f16",
                    "f17", "f18", "f19", "f20"]].values.reshape(len(data), 1, 20)
base_y = data["label"].values.reshape(len(data), 1)

result = model.predict([base_x, conv_x])

print(result)
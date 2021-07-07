import numpy as np
import pandas as pd
import xlrd
import xlwt
from keras.models import load_model
import dataFunction
import matlab.engine
import kwargs
import matplotlib.pyplot as plt


model = load_model(kwargs.DNN.test_model)
print("模型加载完毕！")
data = xlrd.open_workbook("./temp/arc_eva_temp.xls")
area = data.sheet_by_index(0)
for i in range(1, area.nrows):
    mat = np.array([[area.cell_value(i, 0),
                     area.cell_value(i, 1),
                     area.cell_value(i, 2),
                     area.cell_value(i, 3),
                     area.cell_value(i, 4),
                     area.cell_value(i, 5),
                     area.cell_value(i, 6),
                     area.cell_value(i, 7),
                     area.cell_value(i, 8),
                     area.cell_value(i, 9),
                     area.cell_value(i, 12),
                     area.cell_value(i, 13),
                     area.cell_value(i, 14),
                     area.cell_value(i, 15),
                     area.cell_value(i, 22),
                     area.cell_value(i, 23),
                     area.cell_value(i, 24),
                     area.cell_value(i, 25),
                     area.cell_value(i, 26),
                     area.cell_value(i, 27),
                     area.cell_value(i, 28),
                     area.cell_value(i, 29)]])
    df = pd.DataFrame(mat)
    j = model.predict(df)
    print(j)
import numpy as np
import pandas as pd
import xlrd
from keras.models import load_model
import dataFunction
import matlab.engine
import kwargs

print("正在初始化matlab组件......")
eng = matlab.engine.start_matlab()
path = "D:/6A333M/5V-3A-LSD"
fileList = dataFunction.file_name(path, ".mat")
print("matlab组件初始化完毕!")
model = load_model("model.h5")
print("模型加载完毕！")
for matFile in fileList:
    print("正在处理数据......")
    t = eng.matlabPre(matFile)

    dataFunction.matlabFeaSolve(t, len(t))

    data = xlrd.open_workbook("temp.xls")
    area = data.sheet_by_index(0)

    arc = 1
    normal = 0
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
                         area.cell_value(i, 9)]])
        df = pd.DataFrame(mat)
        if model.predict(df) > kwargs.predict.judge_val:
            arc += 1
        else:
            normal += 1
    print(matFile)
    print("异常点个数为：" + str(arc), "正常点个数为" + str(normal), "异常比为" + str(100 * arc / (normal + arc)) + "%", "\n")

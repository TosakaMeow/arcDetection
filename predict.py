import numpy as np
import pandas as pd
import xlrd
import xlwt
from keras.models import load_model
import dataFunction
import matlab.engine
import kwargs

wb = xlwt.Workbook()
sh = wb.add_sheet('1')

print("正在初始化matlab组件......")
eng = matlab.engine.start_matlab()

fileList = dataFunction.file_name(kwargs.DNN.predictPath, ".mat")
print("matlab组件初始化完毕!")
model = load_model("model.h5")
print("模型加载完毕！")
ss = 0
for matFile in fileList:
    print("正在处理数据......")
    t = eng.matlabPre(matFile)

    dataFunction.matlab_solve(t, len(t))

    data = xlrd.open_workbook(kwargs.matlab_slove.temp_path)
    area = data.sheet_by_index(0)

    arc = 1
    normal = 0
    for i in range(1, area.nrows):
        mat = np.array([[area.cell_value(i, 1),
                         area.cell_value(i, 2),
                         area.cell_value(i, 3),
                         area.cell_value(i, 4),
                         area.cell_value(i, 5),
                         area.cell_value(i, 6),
                         area.cell_value(i, 7),
                         area.cell_value(i, 8),
                         area.cell_value(i, 9),
                         area.cell_value(i, 11),
                         area.cell_value(i, 12),
                         area.cell_value(i, 13),
                         area.cell_value(i, 14),
                         area.cell_value(i, 15),
                         area.cell_value(i, 16),
                         area.cell_value(i, 18),
                         area.cell_value(i, 19),
                         area.cell_value(i, 20),
                         area.cell_value(i, 21),]])
        df = pd.DataFrame(mat)
        j = model.predict(df)
        # print(j)

        sh.write(ss, 0, float(j)*10000)
        ss += 1
        if j > kwargs.predict.judge_val:
            arc += 1
        else:
            normal += 1
    print(matFile)
    print("异常点个数为：" + str(arc), "正常点个数为" + str(normal), "异常比为" + str(100 * arc / (normal + arc)) + "%", "\n")
wb.save(kwargs.predict.predict_val_path)


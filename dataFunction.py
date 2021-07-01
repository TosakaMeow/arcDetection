import matlab.engine
import os
import numpy as np
import pandas as pd
import xlrd
import xlwt
import keras
import matlab.engine
import kwargs

def start_matlab(path):
    # 调用matlab进行处理
    print("正在初始化matlab组件......")
    eng = matlab.engine.start_matlab()
    print("matlab组件初始化完毕，正在处理数据......")
    t = eng.matlabPre(path)
    return t


def load_xlsx(path):
    data = xlrd.open_workbook(path)
    area = data.sheet_by_index(0)
    return area


def file_solve(data, data_range):
    # 创建结果存储文件
    wb = xlwt.Workbook()
    sh = wb.add_sheet('1')
    for i in range(0, int(data_range / 500)):
        c0 = 0
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 = 0
        for k in range(i * 500, (i + 1) * 500):
            val = data.cell_value(k, 0)
            if int(val) < 10000:
                c0 += 1
            elif 10000 <= int(val) < 20000:
                c1 += 1
            elif 20000 <= int(val) < 30000:
                c2 += 1
            elif 30000 <= int(val) < 40000:
                c3 += 1
            elif 40000 <= int(val) < 50000:
                c4 += 1
            elif 50000 <= int(val) < 60000:
                c5 += 1
            elif 60000 <= int(val) < 70000:
                c6 += 1
            elif 70000 <= int(val) < 80000:
                c7 += 1
            elif 80000 <= int(val) < 90000:
                c8 += 1
            elif 90000 <= int(val) < 100000:
                c9 += 1
        sh.write(i, 0, c0)
        sh.write(i, 1, c1)
        sh.write(i, 2, c2)
        sh.write(i, 3, c3)
        sh.write(i, 4, c4)
        sh.write(i, 5, c5)
        sh.write(i, 6, c6)
        sh.write(i, 7, c7)
        sh.write(i, 8, c8)
        sh.write(i, 9, c9)
        # print("已完成", int(100*i/int(xlsxData.nrows / 1000)), "%")
    # print("已完成 100 %")

    wb.save('result/data_temp.xls')


def matlab_solve(data, data_range):
    print("正在进行特征采样......")
    # 创建结果存储文件
    wb = xlwt.Workbook()
    sh = wb.add_sheet('1')
    for i in range(0, int(data_range / 500)):
        c0 = 0
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 = 0
        for k in range(i * 500, (i + 1) * 500):
            val = data[k][0]
            if int(val) < 2000:
                c0 += 1
            elif 2000 <= int(val) < 4000:
                c1 += 1
            elif 4000 <= int(val) < 6000:
                c2 += 1
            elif 6000 <= int(val) < 8000:
                c3 += 1
            elif 8000 <= int(val) < 10000:
                c4 += 1
            elif 10000 <= int(val) < 12000:
                c5 += 1
            elif 12000 <= int(val) < 14000:
                c6 += 1
            elif 14000 <= int(val) < 16000:
                c7 += 1
            elif 16000 <= int(val) < 18000:
                c8 += 1
            elif 18000 <= int(val) < 20000:
                c9 += 1
        sh.write(i, 0, c0)
        sh.write(i, 1, c1)
        sh.write(i, 2, c2)
        sh.write(i, 3, c3)
        sh.write(i, 4, c4)
        sh.write(i, 5, c5)
        sh.write(i, 6, c6)
        sh.write(i, 7, c7)
        sh.write(i, 8, c8)
        sh.write(i, 9, c9)
        # print("已完成", int(100*i/int(xlsxData.nrows / 1000)), "%")
    # print("已完成 100 %")

    wb.save('./temp/matlab_temp.xls')


def file_name(file_dir, file_type):
    l = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == str(file_type):
                l.append(os.path.join(root, file))
    return l


def predicr_main(path, log_window):
    wb = xlwt.Workbook()
    sh = wb.add_sheet('1')


    print("正在初始化matlab组件......")
    eng = matlab.engine.start_matlab()

    print("matlab组件初始化完毕!")
    try:
        model = keras.models.load_model("model.odl.h5")
        print("模型加载完毕！")
    except:
        print("模型加载失败！")
    ss = 0
    print("正在处理数据......")
    t = eng.matlabPre(path)

    matlab_solve(t, len(t))

    data = xlrd.open_workbook("./temp/matlab_temp.xls")
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
        j = model.predict(df)
        sh.write(ss, 0, float(j) * 10000)
        ss += 1
        arc = arc+float(j)
        '''
        if j > kwargs.predict.judge_val:
            arc += 1
        else:
            normal += 1
    print("异常点个数为：" + str(arc), "正常点个数为" + str(normal), "异常比为" + str(100 * arc / (normal + arc)) + "%", "\n")
    '''
    print(arc)
    wb.save('预测值统计.temp.xls')

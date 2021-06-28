import xlwt
import xlrd
import matlab.engine

def startMatlab(path):
    # 调用matlab进行处理
    print("正在初始化mablab组件......")
    eng = matlab.engine.start_matlab()
    print("matlab组件初始化完毕，正在处理数据......")
    t = eng.matlabPre(path)
    return t

def loadXlsx(path):
    data = xlrd.open_workbook(path)
    area = data.sheet_by_index(0)
    return area


def fileFeaSolve(data, dataRange):
    # 创建结果存储文件
    wb = xlwt.Workbook()
    sh = wb.add_sheet('1')
    for i in range(0, int(dataRange / 500)):
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

    wb.save('result/data_temp.xls')
def matlabFeaSolve(data, feature, dataRange):
    print("正在进行特征采样......")
    # 创建结果存储文件
    wb = xlwt.Workbook()
    sh = wb.add_sheet('1')
    for i in range(0, int(dataRange / 500)):
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

    wb.save('data_temp.xls')
    # 处理特征数组
    wb1 = xlwt.Workbook()
    sh1 = wb1.add_sheet('1')

    for m in range(0, 5):
        for i in range(0, int(dataRange / 500)):
            c0 = 0
            for k in range(i * 500, (i + 1) * 500):
                val = feature[k][0]
                if int(val) == 1:
                    c0 += 1
            sh1.write(i, m, c0)

    wb1.save('feature_temp.xls')


import os


def file_name(file_dir, fileType):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == str(fileType):
                L.append(os.path.join(root, file))
    return L
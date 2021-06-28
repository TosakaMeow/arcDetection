import xlwt
import xlrd
import matlab.engine
import dataFunction
# l = dataFunction.file_name("featureData", ".xlsx")
# print(l)
data = dataFunction.loadXlsx("./preData/data_A3.xlsx")
dataRange = data.nrows
dataFunction.fileFeaSolve(data, dataRange)

feature = dataFunction.loadXlsx("./preData/feature_A3.xlsx")
featureRange = feature.nrows

wb = xlwt.Workbook()
sh = wb.add_sheet('1')

for m in range(0, 5):
    for i in range(0, int(featureRange / 500)):
        c0 = 0
        for k in range(i * 500, (i + 1) * 500):
            val = feature.cell_value(k, m)
            if int(val) == 1:
                c0 += 1
        sh.write(i, m, c0)

wb.save('result/feature_A3_temp.xls')



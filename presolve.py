import xlwt
import xlrd
import matlab.engine
import dataFunction
# l = dataFunction.file_name("featureData", ".xlsx")
# print(l)
data = dataFunction.loadXlsx("./featureData/data_DZ600.xlsx")
dataRange = data.nrows
dataFunction.fileFeaSolve(data, dataRange)

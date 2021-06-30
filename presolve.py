import xlwt
import xlrd
import matlab.engine
import dataFunction
# l = dataFunction.file_name("featureData", ".xlsx")
# print(l)
data = dataFunction.load_xlsx("./featureData/data_DZ600.xlsx")
dataRange = data.nrows
dataFunction.file_solve(data, dataRange)

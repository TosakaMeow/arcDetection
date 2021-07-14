import xlwt
import pandas as pd
import kwargs


def pretreat_main(source_data, temp_data):
    arc_data = pd.read_csv(source_data)
    arc_frame = arc_data.shape
    wb = xlwt.Workbook()
    f1 = wb.add_sheet('1')
    for i in range(0, int(arc_frame[0] / kwargs.DNN.judge_window)):
        c0 = 0
        c1 = 0
        c2 = 0
        for k in range(i * kwargs.DNN.judge_window, (i + 1) * kwargs.DNN.judge_window):
            val = arc_data["area"][k]
            c0 += val
        for k in range(i * kwargs.DNN.judge_window, (i + 1) * kwargs.DNN.judge_window):
            val = arc_data["low"][k]
            c1 += val
        for k in range(i * kwargs.DNN.judge_window, (i + 1) * kwargs.DNN.judge_window):
            val = arc_data["high"][k]
            c2 += val

        f1.write(i, 0, c0)
        f1.write(i, 1, c1)
        f1.write(i, 2, c2)
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
        for k in range(i * kwargs.DNN.judge_window, (i + 1) * kwargs.DNN.judge_window):
            val = arc_data["low"][k] * 3
            # print(val)
            if val < 0.1:
                c0 += 1
            elif 0.1 <= val < 0.2:
                c1 += 1
            elif 0.2 <= val < 0.3:
                c2 += 1
            elif 0.3 <= val < 0.4:
                c3 += 1
            elif 0.4 <= val < 0.5:
                c4 += 1
            elif 0.5 <= val < 0.6:
                c5 += 1
            elif 0.6 <= val < 0.7:
                c6 += 1
            elif 0.7 <= val < 0.8:
                c7 += 1
            elif 0.8 <= val < 0.9:
                c8 += 1
            elif 0.9 <= val < 1.0:
                c9 += 1
            cell = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]
        f1.write(i, 3, cell[0])
        f1.write(i, 4, cell[1])
        f1.write(i, 5, cell[2])
        f1.write(i, 6, cell[3])
        f1.write(i, 7, cell[4])
        f1.write(i, 8, cell[5])
        f1.write(i, 9, cell[6])
        f1.write(i, 10, cell[7])
        f1.write(i, 11, cell[8])
        f1.write(i, 12, cell[9])
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
        for k in range(i * kwargs.DNN.judge_window, (i + 1) * kwargs.DNN.judge_window):
            val = arc_data["high"][k] * 3
            # print(val)
            if val < 0.1:
                c0 += 1
            elif 0.1 <= val < 0.2:
                c1 += 1
            elif 0.2 <= val < 0.3:
                c2 += 1
            elif 0.3 <= val < 0.4:
                c3 += 1
            elif 0.4 <= val < 0.5:
                c4 += 1
            elif 0.5 <= val < 0.6:
                c5 += 1
            elif 0.6 <= val < 0.7:
                c6 += 1
            elif 0.7 <= val < 0.8:
                c7 += 1
            elif 0.8 <= val < 0.9:
                c8 += 1
            elif 0.9 <= val < 1.0:
                c9 += 1
            cell = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]
        f1.write(i, 13, cell[0])
        f1.write(i, 14, cell[1])
        f1.write(i, 15, cell[2])
        f1.write(i, 16, cell[3])
        f1.write(i, 17, cell[4])
        f1.write(i, 18, cell[5])
        f1.write(i, 19, cell[6])
        f1.write(i, 20, cell[7])
        f1.write(i, 21, cell[8])
        f1.write(i, 22, cell[9])
    wb.save(temp_data)



pretreat_main("./featureData/normal_data.csv", "./temp/normal_temp.xls")
pretreat_main("./featureData/arc_data.csv", "./temp/arc_temp.xls")
pretreat_main("./featureData/normal_test_data.csv", "./temp/normal_test_temp.xls")
pretreat_main("./featureData/arc_test_data.csv", "./temp/arc_test_temp.xls")

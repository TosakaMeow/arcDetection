class DNN:
    epochs = 5  # 训练轮次
    predictPath = "D:/DataSource/train_data/arc"  # 预测场景选取
    judge_window = 100
    test_model = "model.test.h5"


class predict:
    judge_val = 0.80  # 判断阈值
    predict_val_path = "./temp/预测值统计.temp.xls"


class matlab_slove:
    temp_path = './temp/matlab_temp.xls'

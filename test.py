import numpy as np
import pandas as pd
import xlrd
import xlwt
from keras.models import load_model
import dataFunction
import matlab.engine
import kwargs
model = load_model("model.h5")
mat = np.array([[234,43,40,0,0,334,10,14,18,14,21,27,22,16,14]])
df = pd.DataFrame(mat)
t = model.predict(df)
print(t)
import numpy as np
import pandas as pd
import xlrd
import xlwt
from keras.models import load_model
import dataFunction
import matlab.engine
import kwargs
import train

dataFunction.predicr_main("D:/6A333M/5V-3A-30M/30m-2.tdms.mat")
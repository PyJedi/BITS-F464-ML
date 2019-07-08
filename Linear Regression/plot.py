'''
***plotting Average values of RMSE and MMRE for each model***

Author :
Pranath Reddy
2016B5A30572H
'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# import data
# 1 - corr_coef, 2 - gradient_descent, 3 - SciPy
rmse1 = pd.read_csv("2016B5A30572H_RMSE_1.csv",header=None)
rmse2 = pd.read_csv("2016B5A30572H_RMSE_2.csv",header=None)
rmse3 = pd.read_csv("2016B5A30572H_RMSE_3.csv",header=None)
mmre1 = pd.read_csv("2016B5A30572H_MMRE_1.csv",header=None)
mmre2 = pd.read_csv("2016B5A30572H_MMRE_2.csv",header=None)
mmre3 = pd.read_csv("2016B5A30572H_MMRE_3.csv",header=None)

# Rectify NaN values
rmse1 = rmse1.interpolate()
rmse2 = rmse2.interpolate()
rmse3 = rmse3.interpolate()
mmre1 = mmre1.interpolate()
mmre2 = mmre2.interpolate()
mmre3 = mmre3.interpolate()

# finding average of each row
rmse1_av = rmse1.mean(axis=1)
rmse1_av = rmse1_av.as_matrix()
rmse2_av = rmse2.mean(axis=1)
rmse2_av = rmse2_av.as_matrix()
rmse3_av = rmse3.mean(axis=1)
rmse3_av = rmse3_av.as_matrix()

mmre1_av = mmre1.mean(axis=1)
mmre1_av = mmre1_av.as_matrix()
mmre2_av = mmre2.mean(axis=1)
mmre2_av = mmre2_av.as_matrix()
mmre3_av = mmre3.mean(axis=1)
mmre3_av = mmre3_av.as_matrix()

# Plotting
plt.plot(rmse1_av,label='Corr_Coef')
plt.plot(rmse2_av,label='Gradient_Descent')
plt.plot(rmse3_av,label='SciPy')
plt.ylabel('average of RMSE')
plt.xlabel('index of input data')
plt.legend()
plt.show()
plt.close()

plt.plot(mmre1_av,label='Corr_Coef')
plt.plot(mmre2_av,label='Gradient_Descent')
plt.plot(mmre3_av,label='SciPy')
plt.ylabel('average of MMRE')
plt.xlabel('index of input data')
plt.legend()
plt.show()




    


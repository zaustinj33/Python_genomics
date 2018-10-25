#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zaust
#
# Created:     02/08/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# LINEAR REGRESSION ALGO

# BASED ON Y = MX + B

# m = (mean(x) *  mean(y) - mean(x*y)) / ((mean(x))^2 - mean(x)^2)
# b = mean(y) - m*mean(x)

# ERROR FORMULA
# r^2 = 1 - SE(y_hat)/SE(mean(y))

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

#xs = np.array([1,2,3,4,5,6])   #,dtype=np.float64)
#ys = np.array([5,4,5,6,7,8])   #,dtype=np.float64)

def create_dataset(hm,  variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance,1)
        ys.append(y)
    if correlation == 'pos':
        val += step
    elif correlation == 'neg':
        val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype = np.float64)



def best_fit_slope_and_intercept(xs,ys):
    m = ( ((mean(xs) * mean(ys)) - mean(xs*ys)) /
   ( (mean(xs)**2) - mean(xs**2))   )
    b = mean(ys) - m*mean(xs)
    return m, b

def SE(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)

def coef_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    SE_of_reg =  SE(ys_orig, ys_line)
    SE_y_mean =  SE(ys_orig, y_mean_line)
    return 1 - (SE_of_reg /SE_y_mean)

xs, ys = create_dataset(40,80,2,correlation ='neg')

m, b = best_fit_slope_and_intercept(xs,ys)

print(m,b)

regression_line = [(m*x)+b for x in xs]

predict_x = 8
predict_y = (m*predict_x)+b

r_sq = coef_of_determination(ys, regression_line)
print(r_sq)

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y,s=100, color = 'g')
plt.plot(xs, regression_line)
plt.show()


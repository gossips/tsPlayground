# -*- coding: utf-8 -*-

#%% Load dependencies
from numpy import array
from numpy import linspace, exp, cos, sin

from ts_tools import *

import math as mt
import matplotlib.pyplot as plt

#%% Generate test time series
T = 20
t = linspace(0, 10*T, num = 500)
x = cos(2*mt.pi*t/T)
y = sin(2*mt.pi*t/T)

#%% Plot time series
plt.figure()
plt.scatter(t,x)
plt.scatter(t,y)
plt.title('Time series')
plt.ion()
plt.show()

#%% Execute functions
m = mean(x)
c = cov(x,y)
cr = corr(x,y)
v = var(x)
s = sd(x)
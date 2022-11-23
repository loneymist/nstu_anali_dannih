from numpy import exp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sympy import Float


data = pd.read_csv('МатематическиеМетоды/fourier.dat',sep='\t')
print(data)
data.columns = ['X','Y']
values_x = np.array(data['X'])
values_y = np.array(data['Y'])
print(values_x)

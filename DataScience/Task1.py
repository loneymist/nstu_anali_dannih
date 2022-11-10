from numpy import exp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize

data = pd.read_excel('./data.xlsx')
values_x = np.array(data['x'])
values_y = np.array(data['y'])

def target(s):
    return sum((exp(-(values_x/s)**2)-values_y)**2)
res = minimize(target,np.std(values_y))
sko = res.get('x')
print(f'Дисперсия равна: {sko}')
f = exp(-(values_x/sko)**2)

sum = 0
i=0
while i < len(values_x):
    sum+=(exp(-(values_x[i]/sko)**2))
    i+=1
psz = sum/len(values_x)
print(f'Простое среднее значение функции равно : {psz}')


plt.plot(values_x, values_y, 'b.', ms = 2)
plt.plot(values_x, f, 'r', lw = 2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

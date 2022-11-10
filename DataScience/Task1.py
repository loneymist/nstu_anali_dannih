from numpy import exp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize

data = pd.read_excel('./data.xlsx')
values_x = np.array(data['x'])
values_y = np.array(data['y'])

print('x=',values_x)
print('y=',values_y)

def target(s):
    return sum((exp(-(values_x/s)**2)-values_y)**2)
res = minimize(target,np.std(values_y))

f = exp(-(values_x/0.34613752)**2)

plt.plot(values_x, values_y, 'b^', ms = 2)
plt.plot(values_x, f, 'r', lw = 2)

plt.xlabel('x')
plt.ylabel('y')
plt.show()

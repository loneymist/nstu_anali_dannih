from numpy import exp                          
import numpy as np                             
import matplotlib.pyplot as plt                
import pandas as pd                                                   # Импорт библиотек
from scipy.optimize import minimize            
import sympy as sp                             
from scipy import integrate                    

data = pd.read_excel('DataScience/data.xlsx')    
values_x = np.array(data['x'])                                         #Чтение файла
values_y = np.array(data['y'])

def target(s):                  
    return sum((exp(-(values_x/s)**2)-values_y)**2)                    #Функция для нахождения СКО
res = minimize(target,np.std(values_y))
sko = float(res.get('x'))


print(f'Дисперсия равна: {sko}')                                       #Вывод СКО
f = exp(-(values_x/sko)**2)

# plt.plot(values_x, values_y, 'b.', ms = 2)
# plt.plot(values_x, f, 'r', lw = 2)
# plt.xlabel('x')                                                      #Вывод Графиков
# plt.ylabel('y')
# plt.show()

sum = 0
i=0



while i < len(values_x):
    sum+=(exp(-(values_x[i]/sko)**2))                                  #Поиск Среднего значения функции
    i+=1
psz = sum/len(values_x)
print(f'Простое среднее значение функции равно : {psz}')

x = sp.Symbol('x')
fx = sp.exp(-(x/sko)**2)                                              #Поиск дифференциала
dif = sp.diff(fx, x)
print(f'Дифференциал функции равен: {dif}')

def f(x):
    return (exp(-(x/sko)**2))
v, err = integrate.quad(f, -1, 1)                                     #Поиск интеграла
print(f'Интеграл функции равен: {v}')

print(sp.solve(-16.6929326133439*x*sp.exp(-8.34646630667195*x**2),x))         #Решение уравнения

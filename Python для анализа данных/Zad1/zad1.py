import re
import math as m
import cmath as cm
import time

print('Input chislo')
i = 0
top_border = 1000000
num = ''

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

#Проверка корректности ввода данных
while num.isnumeric() == False and isfloat(num) == False: 
    num = input()
num = float(num)

#Вычисление квадратного корня в библиотеке math
t1 = time.time()
while i < top_border:
    m.sqrt(num)
    i+=1
i=0
t2 = time.time()
sqrt1 = t2-t1

#Вычисление квадратного корня в библиотеке cmath
t1 = time.time()
while i < top_border:
    cm.sqrt(num)
    i+=1
i=0
t2 = time.time()
sqrt2 = t2-t1

#Вычисление синуса в библиотеке math
t1 = time.time()
while i < top_border:
    m.sin(num)
    i+=1
i=0
t2 = time.time()
sin1 = t2-t1

#Вычисление синуса в библиотеке cmath
t1 = time.time()
while i < top_border:
    m.sin(num)
    i+=1
i=0
t2 = time.time()
sin2 = t2-t1

#Вычисление логарифма в библиотеке math
t1 = time.time()
while i < top_border:
    m.log(num)
    i+=1
i=0
t2 = time.time()
log1 = t2-t1

#Вычисление логарифма в библиотеке cmath
t1 = time.time()
while i < top_border:
    cm.log(num)
    i+=1
i=0
t2 = time.time()
log2 = t2-t1

#Вывод данных
print('Math sqrt:',sqrt1,'|| CM SQRT: ',sqrt2, '\nM sin:',sin1, '|| CM sin:',sin2,'\nM log:',log1,'|| CM log',log2)
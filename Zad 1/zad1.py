import re
import math as m
import cmath as cm
import time
print('Input chislo')
i = 0
num = 'aaa'

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while num.isnumeric() == False and isfloat(num) == False:
    num = input()
num = float(num)
#math sqrt
t1 = time.time()
while i < 1000000:
    m.sqrt(num)
    i+=1
i=0
t2 = time.time()
sqrt1 = t2-t1

#cmath sqrt
t1 = time.time()
while i < 1000000:
    cm.sqrt(num)
    i+=1
i=0
t2 = time.time()
sqrt2 = t2-t1

#math sin
t1 = time.time()
while i < 1000000:
    m.sin(num)
    i+=1
i=0
t2 = time.time()
sin1 = t2-t1

#cmath sin
t1 = time.time()
while i < 1000000:
    m.sin(num)
    i+=1
i=0
t2 = time.time()
sin2 = t2-t1

#math log
t1 = time.time()
while i < 1000000:
    m.log(num)
    i+=1
i=0
t2 = time.time()
log1 = t2-t1

#cmath log
t1 = time.time()
while i < 1000000:
    cm.log(num)
    i+=1
i=0
t2 = time.time()
log2 = t2-t1
print('Math sqrt: ',sqrt1,'|| CM SQRT: ',sqrt2, '\nM sin:',sin1, '|| CM sin:',sin2,'\nM log:',log1,'|| CM log',log2)


with open(r'table.txt','w') as data:
    data.write(r'sqrt time CMATH sqrt time MATH sin time CMATH sin time Math log time Cmath log time'+'\n')
    data.write(r'' + str(round(sqrt1,7)) + ' ' + str(round(sqrt2,13)) + ' ' + str(round(sin1,11)) + ' ' + str(round(sin2,12)) + ' ' + str(round(log1,11)) + ' ' + str(round(log2,12)))
import math
with open(r'Zad3\complex.txt','r') as data: #Открытие файла с исходными данными

    nums = []
    print('Enter the comparison num:')
    comp = float(input())   #Ввод числа для сравнения
    lines = data.readlines()
    c=0
    i=0

    for line in lines:
        nums.append(complex(line.strip())) #Заполнение списка комплексными данными
    
    print('\nLower than entered:\n')
    while i < len(nums):
        if math.sqrt(nums[i].real*nums[i].real+nums[i].imag*nums[i].imag) < comp: #Проверка на то, является ли модуль комплексного числа меньше заданного пользователем
            print(nums[i])
        i+=1
    i = 0
    print('\nHigher than entered:\n')
    while i < len(nums):
        if math.sqrt(nums[i].real*nums[i].real+nums[i].imag*nums[i].imag) > comp: #Проверка на то, является ли модуль комплексного числа больше заданного пользователем
            print(nums[i])
        i+=1
    i = 0
    print('\nEqual to your Num:\n')
    while i < len(nums):
        if math.sqrt(nums[i].real*nums[i].real+nums[i].imag*nums[i].imag) == comp: #Проверка на то, является ли модуль комплексного числа равным заданному пользователем
            print(nums[i])
        i+=1
    data.close
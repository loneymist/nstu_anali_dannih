check = lambda list,i,c = 0: c+1 if type(list[i]) == type(list[i-1]) else c-0

dict_out = {}               #задание пустого словаря

p = False                   #проверка на количество введенных данных
while p == False:
    print('--- ВВОД ДАННЫХ ---')
    list = input('Введите данные (3-5 значений) через пробел:').split() #разделение введенных данных через пробел в список
    if len(list)>= 3 and len(list)<=5: p = True                         #проверяем длину словаря
    else: print('Неверное кол-во элементов.')
prov = 0

for i in range(0,len(list)):                    #проверка на типы данных, используя цикл
    if '.' in list[i]:
        try: 
            list[i]=float(list[i])              #проверка на тип float, иначе str
        except ValueError:
            list[i] = str(list[i])
    else: 
        try: 
            list[i]=int(list[i])                #проверка на тип int, иначе str
        except ValueError:
            list[i] = str(list[i])
    prov += check(list,i)                       #узнаем количество одинаковых элементов, проверенных выше через лямбда функцию
if prov == len(list)-1:                         
    for i in range(0,len(list)):                #если все ок, обновляем наш словарь проверенными одинаковыми элементами
        dict_out.update({i:list[i]})
else: 
    print('Типы различаются')
    for i in range(0,len(list)):                #иначе обновляем наш словарь всеми типами данных, присваивая им тип str
        dict_out.update({i:str(list[i])})

print(dict_out,type(dict_out.get(0)))           #выводим словарь и его тип

with open('Zad2_Out.txt','w') as data:          #записываем результат в файл вместе с типом данных
    data.writelines(str(dict_out.items()) + '\n')
    data.write(str(type(dict_out.get(0))))
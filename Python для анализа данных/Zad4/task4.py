def fun(*nums,r = 0):                       #Определение функции.

    try:                                    #Вывод const, если кол-во входных данных равно нулю.
        r += nums[0]
    except IndexError:
        print('const')
        
    if len(nums) == 1:                      #Вывод ошибки, если кол-во входных данных равно одному.
        print('Error (only 1 argument)')

    if len(nums) > 3:                       #Вывод ошибки, если кол-во входных больше, чем три.
        print('Error (>3 arguments)')

    sum = 0
    multi = 1

    for n in nums: 
        if len(nums) == 2:                  #Сложение, если кол-во входных данных равно двум.
            sum += n

        if len(nums) == 3:                  #Умножение, если кол-во входных данных равно четырём.
            multi *= n
        

    if len(nums) == 2:                      #Вывод суммы, если кол-во входных данных равно двум.
        print('Sum: ',sum)

    if len(nums) == 3:
        print('Multiplipaction: ',multi)    #Вывод умножения, если кол-во входных данных равно четырём.

#Проверки
fun()
fun(1.0)
fun(1.0,5.0)
fun(2.0,5,7)
fun(2.0,5,7,8)

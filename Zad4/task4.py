from tkinter import N


def fun(*nums):
    sum = 0
    multi = 1
    for n in nums:
        if nums == None:
            print('const')
            break
        if len(nums) == 1:
            print('Error (only 1 argument)')
            break
        if len(nums) > 3:
            print('Error (>3 arguments)')
            break
        if len(nums) == 2:
            sum += n
        if len(nums) == 3:
            multi *= n

    if len(nums) == 2:
        print('Sum: ',sum)
    if len(nums) == 3:
        print('Multiply: ',multi)


fun()
fun(1.0)
fun(1.0,5.0)
fun(2.0,5,7)
fun(2.0,5,7,8)
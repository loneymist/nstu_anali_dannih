from multiprocessing.resource_sharer import stop

def fun(*nums,r = 0):
    try:
        r += nums[0]
    except IndexError:
        print('const')
    if len(nums) == 1:
        print('Error (only 1 argument)')
        stop()
    if len(nums) > 3:
        print('Error (>3 arguments)')
        stop()
    sum = 0
    multi = 1
    for n in nums: 
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
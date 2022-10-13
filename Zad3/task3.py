import math
with open(r'Zad3\complex.txt','r') as data:
    nums = []
    print('Enter the comparison num:')
    comp = float(input())
    lines = data.readlines()
    c=0
    i=0
    for line in lines:
        nums.append(complex(line.strip()))
    print('\nLower than entered:\n')
    while i < len(nums):
        if math.sqrt(nums[i].real*nums[i].real+nums[i].imag*nums[i].imag) < comp:
            print(nums[i])
        i+=1
    i = 0
    print('\nHigher than entered:\n')
    while i < len(nums):
        if math.sqrt(nums[i].real*nums[i].real+nums[i].imag*nums[i].imag) > comp:
            print(nums[i])
        i+=1
    i = 0
    print('\nEqual to your Num:\n')
    while i < len(nums):
        if math.sqrt(nums[i].real*nums[i].real+nums[i].imag*nums[i].imag) == comp:
            print(nums[i])
        i+=1
    data.close
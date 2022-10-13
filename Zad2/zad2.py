with open(r'Zad2\Res.txt','w') as data:
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def isint(value):
        try:
            int(value)
            return True
        except ValueError:
            return False
    n = 0
    i=0
    c = 0
    c1 = 0
    list = []

    while float(n) < 3 or float(n) > 5:
        print('How much elements do you want? (3-5)')
        n = input()
    while i<int(n):
        print('Enter',i+1,'element of list')
        list.append(input())
        i+=1
    print('Your list:',list)
    data.write(r'Your list'+str(list)+'\n')
    i = 0
    while i < int(n):
        if isfloat(list[i]) == True and '.' in list[i]:
            c+=1
        if isint(list[i]) == True:
            c1+=1
        i+=1
    i = 0
    if c == int(n):
        print('All elemets are "Float" type')
        data.write(r'All elemets are "Float" type')
    if c1 == int(n):
        print('All elements are "Int" type')
        data.write(r'All elements are "Int" type')
    if c1 != int(n) and c!= int(n):
        print('Your elements are not similar type')
        data.write(r'Your elements are not similar type')
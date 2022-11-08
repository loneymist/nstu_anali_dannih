import pandas

data = pandas.read_excel("C:/Users/abobu/.vscode/NGTU/KURSI/GIT/nstu_anali_dannih-1/DataScience/data.xlsx")
data.head()
y1 = []
y = []
x = []
for i in data.values:
    temp = str(i)
    temp = temp.replace('[','') 
    temp = temp.replace(']','') 
    temp = temp.split()
    x.append(float(temp[0]))
    y.append(float(temp[1]))
print('x =',x)
print('y = ',y)
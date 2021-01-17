arr = []
for i in range(9):
    arr.append(input())

if arr.count('Lion') >= 5 or arr.count('Tiger') >= 5:
    if arr.count('Lion') > arr.count('Tiger'):
        print('Lion')
    else:
        print('Tiger')

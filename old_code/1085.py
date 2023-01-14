import math

arr = []
x, y, w, h = list(map(int, input().split()))

arr.append(math.sqrt(pow((x-w), 2)+pow((y-h), 2)))
arr.append(math.sqrt(pow((x-w), 2)+pow((y), 2)))
arr.append(math.sqrt(pow((x), 2)+pow((y-h), 2)))
arr.append(math.sqrt(pow((x), 2)+pow((y), 2)))
print(min(arr))

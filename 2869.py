import math

a, b, v = list(map(int, input().split()))

n = (((v-a)/(a-b))+1)


print(math.ceil(n))

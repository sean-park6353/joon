arr = list(map(int, input().split()))
b = [i**2 for i in arr]
print(sum(b) % 10)

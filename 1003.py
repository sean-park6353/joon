def fibonacci(n):
    if n == 0:
        print('0')
        return 0
    elif n == 1:
        print('1')
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n = input()
arr = []

for i in range(int(n)):
    arr.append(int(input()))

print("="*15)
fibonacci(arr[0])
print("="*15)
fibonacci(arr[1])
print("="*15)
fibonacci(arr[2])

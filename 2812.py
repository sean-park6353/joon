# a, b = map(int, input().split())
# num = list(map(int, input()))
# r = []
# for i in range(b):
#     r.append(min(num))
#     num.remove(min(num))

# for i in len(num):
#     print(num[i], end='')


# def combinations(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations(arr[i+1:], r-1):
#                 yield [arr[i]] + next


from itertools import combinations
a, b = map(int, input().split())
num = list(map(int, input()))





# combi = combinations(num, len(num)-b)
# result = max(list(combi))

# tmp = list(result)
# for i in range(len(tmp)):
#     print(tmp[i], end='')

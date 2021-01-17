arr = []
for i in range(5):
    tmp = int(input())
    arr.append(tmp)

free_a = (arr[-1]-30)*arr[1]
free_b = (arr[-1]-45)*arr[3]
if free_a < 0:
    free_a = 0
if free_b < 0:
    free_b = 0
print(arr[0]+free_a*21)
print(arr[2]+free_b*21)

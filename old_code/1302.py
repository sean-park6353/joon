n = int(input())
archive = []
for i in range(n):
    archive.append(input())
archive.sort()
result = []
for i in range(n):
    result.append(archive.count(archive[i]))
print(archive[result.index(max(result))])

graph=[]
for i in range(5):
    graph.append(list(map(str,input().strip())))
    # graph.append(list(map(str,input().strip())))

answer=[]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if j>=i:
            answer.append('')
        else:
            answer.append(graph[j][i])
        

for i in answer:
    print(i,end='')

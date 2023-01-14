
a,b=map(int,input().split())
graph=[]
for i in range(a):
    graph.append(list(map(int,input().split())))
xpos=[-1,1,0,0]
ypos=[0,0,-1,1]
visit=[[False]*b for _ in range(a)]

cnt=0
def dfs(x,y):
    visit[x][y]=True
    for i in range(4):
        new_x=x+xpos[i]    
        new_y=y+ypos[i]
        if new_x>=a or new_y>=b or new_x<0 or new_y<0:
            continue
        if visit[new_x][new_y]==True:
            continue
        if graph[new_x][new_y]==0:
            graph[x][y]=graph[x][y]-1
            if graph[x][y]<0:
                graph[x][y]=0
            continue
        dfs(new_x,new_y)

answer=0
while True:
    show=0
    flg=False
    for i in range(a):
        show+=sum(graph[i])
    if show==0:
        # answer=0
        break
    # for i in range(a):
    #     for j in range(b):
    #         if graph[i][j]**2!=0:
    #             x,y=i,j
    #             if graph[x-1][y]==0 and graph[x][y+1]==0 and graph[x][y-1]==0 and graph[x+1][y]==0:
    #                 flg=True
    #                 break
    #     if flg==True:
    #         break
    # if flg==True:
    #     break
    for i in graph:
        print(i)
    print()
    cho=False
    visit=[[False]*b for _ in range(a)]
    for i in range(a):
        for j in range(b):
            if graph[i][j]!=0 and visit[i][j]==False:
                cho=True
                p,q=i,j
                break
        if cho==True:
            break
    dfs(i,j)
    answer+=1     
print(answer)

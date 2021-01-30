from collections import deque

a,b=map(int,input().split())
xpos=[-1,1,0,0]
ypos=[0,0,-1,1]
graph=[]
visit=[[0]*b for _ in range(a)]


def bfs(x,y):
    q=deque([(x,y)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            new_x=x+xpos[i]
            new_y=y+ypos[i]
            if new_x<0 or new_y<0 or new_x>=a or new_y>=b:
                continue
            if graph[new_x][new_y]!=1:
                continue
            if visit[new_x][new_y]!=0:
                continue
            visit[new_x][new_y]=visit[x][y]+1
            q.append((new_x,new_y))
    print(visit[a-1][b-1])
for i in range(a):
    graph.append(list(map(int,input().strip())))


visit[0][0]=1
bfs(0,0)

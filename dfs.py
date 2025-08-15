def DFS(adj_list,v):
    visited=[False]*v
    stack=[0]
    visited[0]=True
    print(0,end=' ')
    while stack:
        cur=stack[-1]
        unvisited_neigh=False
        for i in adj_list[cur]:
            if visited[i]!=True:
                stack.append(i)
                print(i,end=' ')
                visited[i]=True
                unvisited_neigh=True
                break
        if not unvisited_neigh:
            stack.pop()
v=int(input())
if v==0:
    print("Graph doesn't exist")
else:
    adj_list=[[] for i in range(v)]
    while True:
        v1,v2=map(int,input().split())
        if v1!=-1 and v2!=-1:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)
        else:
            break
print("DFS : ",end='')            
DFS(adj_list,v)

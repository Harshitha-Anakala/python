t=int(input())
for i in range(t):
    V,E=map(int,input().split())
    adj_list=[[]for i in range(V)]
    for i in range(E):
        v1,v2=map(int,input().split())
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
    for i in range(V):
        print(i,end=' ')
        for j in adj_list[i]:
            print("->",jend=' ')
           

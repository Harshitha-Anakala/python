# #Directed graph
# v = int(input())
# print("Please enter the number of nodes in the graph")
# e = int(input())
# print("Please enter the number of edges in the graph")
# directed = input().lower() == "yes"    # stores True
# print("Is the graph directed")
# print("Adjacency Matrix Representation:")
# adj_matrix = [[0]*v for i in range(v)]
# for i in range (v):
#     for j in range(v):
#         print(adj_matrix[i][j],end = ' ')
#     print()
# for i in range(v):
#     print(f"Enter the start node, end node and weight of edge no {i+1}")
#     s,e,w = map(int,input().split())
#     s -=1;e -=1
#     if not directed:
#         adj_matrix[s][e] = w
#         adj_matrix[e][s] = w
#     else:
#         adj_matrix[s][e] = w
# print("Adjacency Matrix Representation:")
# for i in range (v):
#     for j in range(v):
#         print(adj_matrix[i][j],end = ' ')
#     print()
    
    
    
v,e=map(int,input().split())
adj_matrix=[[0]*v for i in range(v)]
for i in range(v):
    for j in range(v):
        print(adj_matrix[i][j],end=' ')
    print()
for i in range(e):
    v1,v2=map(int,input().split())
    adj_matrix[v1][v2]=1
    adj_matrix[v2][v1]=1
for i in range(v):
    for j in range(v):
        print(adj_matrix[i][j],end=' ')
    print()
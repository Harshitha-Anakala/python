n = int(input( ))
arr = []
for i in range(n):
    row = list(map(int, input().split())) 
    arr.append(row)  
print("Transpose Matrix is: ")
for i in range(n):
    for j in range(n):
        print(arr[j][i], end=" ")
    print()  

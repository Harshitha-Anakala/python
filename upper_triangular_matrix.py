n = int(input( ))
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
for i in range(n):
    for j in range(i):
        if arr[i][j]!=0:
            print(" Not Upper Triangular matrix.")
            break
    else:
        print("Upper Triangular Matrix")
        break
else:
    print(" Not Upper Triangular Matrix")

    
"""print("\nThe upper triangular matrix is:")
for i in range(n):
    for j in range(n):
        if j <= i:
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ") 
    print()  """
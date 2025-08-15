n = int(input( ))
arr = []
print("Enter the matrix row by row:")
for i in range(n) :   
    row = list(map(int, input().split()))
    arr.append(row)
zigzag_sum = 0
for i in range(n):
    zigzag_sum += arr[0][i]
    print(f"sun of first row{zigzag_sum}")
    zigzag_sum += arr[n-1][i]
    print(zigzag_sum)
for j in range(1, n-1):
        zigzag_sum += arr[i][n-1-i]
print("The zig-zag sum of the matrix is:", zigzag_sum)



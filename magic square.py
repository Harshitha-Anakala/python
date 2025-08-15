matrix = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)
sum1 = sum(matrix[i][i] for i in range(3))
sum2 = sum(matrix[i][2 - i] for i in range(3))
if sum1 == sum2:
    print("Magic Square")
else:
    print("Not a Magic Square")

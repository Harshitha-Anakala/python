n1 = int(input( ))
sum1 = 0
sum2 = 0
for i in range(n1):
    n = int(input( ))
    sum1 += n
n2 = int(input( ))
for j in range(n2):
    n = int(input( ))
    sum2 += n
if sum1 == sum2:
    print("Same")
else:
    print("Not Same")


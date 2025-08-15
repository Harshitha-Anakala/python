n = int(input("Enter n: "))
m = int(input("Enter m: "))
print(f"The multiplication table of {n} is")
for i in range(1, m+1):
    print(f"{n} * {i} = {i * n}")

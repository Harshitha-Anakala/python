d1 = int(input("Enter dollars for the first amount: "))
c1 = int(input("Enter cents for the first amount: "))
d2 = int(input("Enter dollars for the second amount: "))
c2 = int(input("Enter cents for the second amount: "))

c = (c1 + c2) // 100
d = (d1 + d2) + c
a = (c1 + c2) % 100
print(f"Number of dollars are {d} and number of cents are {a}.")
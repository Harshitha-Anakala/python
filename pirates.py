t = int(input("Enter the initial amount: "))
x = int(input("Enter value x: "))
y = int(input("Enter value y: "))

long_beard = t * (x/100)
t1 = t - long_beard
black_beard = t1 * (y/100)
rem = t1 - black_beard
a = rem // 3
b = rem % 3

print(f"Long Beard's amount: {long_beard}")
print(f"Black Beard's amount: {black_beard}")
print(f"Amount for each person: {a}")
print(f"The remaining amount is {b}.")

n = int(input( ))
a = []
for i in range(n):
    element = int(input( ))
    if element not in a:
        a.append(element)
a = len(a)
print(f"There are {a} distinct elements in the array.")

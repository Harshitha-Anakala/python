n = int(input( ))
a = []
for i in range(n):
    element = int(input( ))
    if element not in a:
        a.append(element)
print(a)
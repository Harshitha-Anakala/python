n=input()
stack=[]
b=True
for i in n:
    if  i in '{([':
        stack.append(i)
    else:
        if not stack:
            b=False
            break
        else:
            a=stack.pop()
            if a=='(' and i!=')' or a=='{' and i!='}' or a=='[' and i!=']':
                b=False
                break
if b and not stack:
    print("Balanced")
else:
    print("Not Balanced")
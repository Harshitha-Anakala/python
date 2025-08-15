postfix_expression = input()
stack=[]
for i in postfix_expression:
    if i.isnumeric():
        stack.append(i)
    else:
        v2 = int(stack.pop())
        v1 = int(stack.pop())
        if i == '+':
            stack.append(v1 + v2)
        elif i == '-':
            stack.append(v1 - v2)
        elif i == '*':
            stack.append(v1 * v2)
        elif i == '/':
            stack.append(v1 // v2) 
print(stack.pop())

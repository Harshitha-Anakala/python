def prio(i):
    if i == '^':
        return 3
    elif i == '*' or i == '/':
        return 2
    elif i == '+' or i == '-':
        return 1
    else:
        return 0

def infix_to_postfix(s):
    oper = []
    char = []
    for i in s:
        if i.isalpha():
            char.append(i)
        elif i == '(':
            oper.append(i)
        elif i ==')':
            while oper and oper[-1] != '(':
                temp = oper.pop()
                char.append(temp)
            if oper:
                oper.pop()
        else:
            while oper and prio(i) <= prio(oper[-1]):
                char.append(oper.pop())     
            oper.append(i)
    while oper:
        char.append(oper.pop())
    return ''.join(char)
s = input()
print(infix_to_postfix(s))
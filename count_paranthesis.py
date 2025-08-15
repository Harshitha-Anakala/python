s=input()
l=[]
l.append(-1)
ans=0
for i in range(len(s)):
    if s[i] == '(':
        l.append(i)
    else:
        if len(l)==0:
            l.append(i)
        else:
            l.pop()
            if len(l)==0:
                l.append(i)
            else:
                ans=max(ans,i-l[-1])
print(ans)
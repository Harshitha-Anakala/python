l=[]
for i in range(1,5):
    l.append(i)
print(l[::-1])

l=[]
s=input()
for i in s:
  l.append(i)
for i in reversed(l):
  print(i,end='')
n=int(input())
l=[]
while n>0:
    l.append(n)
    n=int(input())
if not l:
    print("Queue is empty")
else:
    print("Before Reversing:")
    for i in l:
        print(i,end=' ')
    print("\nafter reversing:")
    for i in reversed(l):
        print(i,end=' ')
        

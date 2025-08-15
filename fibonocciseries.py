month=int(input())
if month<=0:
    print(0)
elif month==1:
    print(0)
elif month==2:
    print(1)
else:
    a=0
    b=1 
    for _ in range(3,month+1):
        a,b=b,a+b 
print(b)
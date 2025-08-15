#n1=[10,98,27,13,4,26,3,11]
#b=[]
#c=[]
#for i in range(len(n1)):
#    if n1[i]%2==0:
 #       b.append(n1[i])
 #   else:
  #      c.append(n1[i])
  
n=[10,98,27,13,4,26,3,11]
a,b = [], []
left, right = 0, len(n) - 1

while left <= right:
    if n[left] % 2 == 0:
        a.append(n[left])  
    else:
        b.append(n[left]) 

    if left != right: 
        if n[right] % 2 == 0:
            a.append(n[right])
        else:
            b.append(n[right])

    left += 1
    right -= 1
result = a + b
print(result)

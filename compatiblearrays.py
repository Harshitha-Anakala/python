n1=int(input())
n2=int(input())
arr1=[]
arr2=[]
if (n1)==(n2):   
   for i in range(n1):
       n=int(input())
       arr1.append(n)
   for j in range(n2):
       n=int(input())
       arr2.append(n)
       if (n1==n2 and arr1[i]>=arr2[j]):
            print("Compatible")
       else:
            print("Not Compatble")
else:
    print("Not Compatible")
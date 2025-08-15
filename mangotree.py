rows=int(input(" "))
columns=int(input(" "))
tree=int(input(" "))
if(tree%columns==0 or tree==1 or tree<=columns ):
    print('mango tree')
else:
    print('other tree')
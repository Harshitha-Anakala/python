class node:
    def __init__(self, data):
        self.data=data
        self.add=None
class ll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.add=self.head
            self.head=newnode
            self.tail=newnode
            
    def display(self):
        while self.head!=None:
            print(self.head.data)
            self.head=self.head.add
obj=ll()
n=int(input())
while True:
    if n>0:
        obj.insert(n)
        n=int(input())
    else:
        break
obj.display()
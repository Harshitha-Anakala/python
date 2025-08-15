class Node:
    def __init__(self, data):
        self.data = data  
        self.add = None  

head = Node("Hey")
obj1 = Node("Wassup")
obj2 = Node("Can")
obj3 = Node("we")
obj4 = Node("meet")

head.add = obj1
obj1.add = obj2
obj2.add = obj3
obj3.add = obj4

print(head.data)          
print(head.add)     
print(obj1.data)          
print(obj1.add)     
print(obj2.data)          
print(obj2.add)     
print(obj3.data)          
print(obj3.add)     
print(obj4.data)          
print(obj4.add)         
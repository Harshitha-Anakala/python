class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if not data:
            return
        
        queue = []
        self.root = node(data[0])
        queue.append(self.root)
        i = 1
        while queue and i < len(data):
            parent = queue.pop(0)
            
            leftvalue = data[i]
            if leftvalue != -1:
                parent.left = node(leftvalue)
                queue.append(parent.left)
            i += 1
            
            if i < len(data):
                rightvalue = data[i]
                if rightvalue != -1:
                    parent.right = node(rightvalue)
                    queue.append(parent.right)
                i += 1
                
    def height(self, root):  
        if root is None:
            return 0  
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1

input_data = list(map(int, input().split()))
object = tree()
object.insert(input_data)
print(object.height(object.root))

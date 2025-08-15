#stack using list
"""from collections import deque
stack=[]
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
print(stack.pop(0))  # we keep 0 in pop because it returns 1st element if not returns lat element
print(stack.pop(0))
print(stack.pop(0))
print(stack.pop(0))"""

#stack using dequeue 
"""from collections import deque
stack=deque()
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
print(stack.pop(0))  # we keep 0 in pop because it returns 1st element if not returns lat element
print(stack.pop(0))
print(stack.pop(0))
print(stack.pop(0))"""

#stack using lifoqueue
from queue import LifoQueue
stack=LifoQueue()
stack.put('a')
stack.put('b')
stack.put('c')
print(stack.qsize())
stack.get('a')
stack.get('b')
stack.get('c')
print(stack.qsize())
print(stack.full())
print(stack.empty())
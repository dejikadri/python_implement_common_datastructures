from collections import deque

"""
    An implementation of a stack using the Deque("double-ended queue") Python data structure
"""
class Stack(object):

    def __init__(self):
        self.items = deque()

    def isEmpty(self):
        return self.items == deque()

    def push(self, item):
        self.items.appendleft(item)

    def pop(self):
        return self.items.popleft()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def show(self):
        return self.items


st = Stack()
st.push('A')
st.push('B')

print(st.show(), st.push('C'), st.size(),   st.peek())
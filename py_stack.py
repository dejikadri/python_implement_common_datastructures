from collections import deque


class Stack(object):
    """
        An implementation of a stack using the Deque("double-ended queue") Python data structure
    """

    def __init__(self):
        self.items = deque()

    def isempty(self):
        return self.items == deque()

    def push(self, item):
        self.items.appendleft(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.popleft()
        else:
            return "Stack is empty!"

    def peek(self):
        if len(self.items) > 0:
            return self.items[0]
        else:
            return "Stack is empty!"

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

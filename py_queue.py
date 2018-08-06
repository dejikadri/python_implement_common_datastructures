from collections import deque


class Queue(object):
    """
        An implementation of a queue using the Deque("double-ended queue") Python data structure
    """

    def __init__(self):
        self.items = deque()

    def isempty(self):
        return self.items == deque()

    def enqueue(self, item):
        self.items.appendleft(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return "Queue is empty!"

    def peekfirstin(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return "Queue is empty!"

    def peeklastin(self):
        if len(self.items) > 0:
            return self.items[0]
        else:
            return "Queue is empty!"

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

from collections import deque

class Queue(object):

    def __init__(self):
        self.items = deque()

    def isEmpty(self):
        return self.items == deque()

    def enqueue(self, item):
        self.items.appendleft(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return "Queue already empty!"

    def peekfirstin(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return "Empty"

    def peeklastin(self):
        if len(self.items) > 0:
            return self.items[0]
        else:
            return "Empty"

    def size(self):
        return len(self.items)

    def show(self):
        return self.items


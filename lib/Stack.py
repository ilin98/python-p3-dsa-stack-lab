class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item) if len(self.items) < self.limit else None
        return self.items

    def pop(self):
        return self.items.pop() if len(self.items) != 0 else None

    def peek(self):
        pass

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for i in range(0, len(self.items)):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1

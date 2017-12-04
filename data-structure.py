class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def divdeBy2(decNumber):
    rs = Stack()

    while decNumber > 0:
        rem = decNumber % 2

        rs.push(rem)
        decNumber = decNumber // 2

    bs = ""
    while not rs.isEmpty():
        bs = bs + str(rs.pop())

    return bs

print(divdeBy2(42))

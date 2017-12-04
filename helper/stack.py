class Stack:
    def __init__(self):
        self.__list = []

    def push(self, key):
        self.__list.append(key)

    def pop(self):
        return self.__list.pop()

    def is_empty(self):
        return len(self.__list) == 0

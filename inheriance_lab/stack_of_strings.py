class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        return '[' + ', '.join([f'{el}' for el in self.data[::-1]]) + ']'


stack = Stack()
stack.push("apple")
stack.push("carrot")
print(str(stack))
stack.pop()
stack.top()
stack.push("cucumber")
print(str(stack))
print(stack.is_empty())
<<<<<<< HEAD
<<<<<<< HEAD
class Stack:
    def __init__(self):
        self.items = []

    # O(1)
    def push(self, item):
        self.items.append(item)

    # O(1)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # O(1)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())
print(stack.peek())
=======

>>>>>>> 4a1d78030ff4edb328f0a3eda5e88afeae75a50b
=======

>>>>>>> 1cc2a77af8da8febd47a62b2a143fc4226b5ff69

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
import math

# Operator precedence
PREC = {
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
    '^': 4
}

# Fungsi matematika
FUNCS = {
    'sin': math.sin,
    'cos': math.cos,
    'sqrt': math.sqrt,
    'log': math.log,
    'abs': abs
}


# ── Node Linked List ─────────────────────────────

class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# ── Stack Linked List ────────────────────────────

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = LLNode(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None

        val = self.top.data
        self.top = self.top.next
        return val

    def is_empty(self):
        return self.top is None

    def to_list(self):
        result = []
        cur = self.top

        while cur:
            result.append(cur.data)
            cur = cur.next

        return result[::-1]


# ── Evaluasi Postfix ─────────────────────────────

def evaluate_postfix(postfix, variables):

    stack = Stack()

    for token in postfix:

        # Jika angka
        if token.replace('.', '', 1).isdigit():
            stack.push(float(token))

        # Jika variabel
        elif token.isalpha() and token not in FUNCS:
            stack.push(float(variables[token]))

        # Jika operator
        elif token in PREC:

            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2

            elif token == '-':
                result = operand1 - operand2

            elif token == '*':
                result = operand1 * operand2

            elif token == '/':
                result = operand1 / operand2

            elif token == '^':
                result = operand1 ** operand2

            stack.push(result)

        # Jika fungsi matematika
        elif token in FUNCS:

            arg = stack.pop()
            result = FUNCS[token](arg)

            stack.push(result)

        # Trace stack
        print(f"Token: {token}")
        print("Stack:", stack.to_list())
        print("-" * 30)

    return stack.pop()


# ── Contoh Penggunaan ────────────────────────────

postfix = ['a', '2', '^', 'b', '2', '^', '+']

variables = {
    'a': 3,
    'b': 4
}

hasil = evaluate_postfix(postfix, variables)

print("Hasil akhir =", hasil)
>>>>>>> feat/fahreza

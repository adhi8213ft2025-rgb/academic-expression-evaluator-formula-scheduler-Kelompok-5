import math


# =========================
# NODE TREE
# =========================
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# =========================
# NODE STACK LINKED LIST
# =========================
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# =========================
# STACK LINKED LIST
# =========================
class Stack:
    def __init__(self):
        self.top_node = None

    def is_empty(self):
        return self.top_node is None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if not self.is_empty():
            temp = self.top_node
            self.top_node = self.top_node.next
            return temp.data
        return None

    def top(self):
        if not self.is_empty():
            return self.top_node.data
        return None


# =========================
# GLOBAL VARIABLE
# =========================
variables = {}
defined_expression = ""


# =========================
# PRECEDENCE
# =========================
def precedence(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    return 0


# =========================
# RIGHT ASSOCIATIVE
# =========================
def is_right_associative(op):
    return op == '^'


# =========================
# INFIX -> POSTFIX
# =========================
def infix_to_postfix(infix):

    stack = Stack()
    output = []

    tokens = infix.split()

    for token in tokens:

        if token.replace('.', '', 1).isdigit() or token.isalpha():
            output.append(token)

        elif token == '(':
            stack.push(token)

        elif token == ')':

            while not stack.is_empty() and stack.top() != '(':
                output.append(stack.pop())

            stack.pop()

        else:

            while (not stack.is_empty() and
                   stack.top() != '(' and
                   (
                       precedence(stack.top()) > precedence(token)
                       or
                       (
                           precedence(stack.top()) == precedence(token)
                           and not is_right_associative(token)
                       )
                   )):

                output.append(stack.pop())

            stack.push(token)

    while not stack.is_empty():
        output.append(stack.pop())

    return output


# =========================
# EVALUASI POSTFIX
# =========================
def evaluate_postfix(postfix):

    stack = Stack()

    for token in postfix:

        # angka
        if token.replace('.', '', 1).isdigit():
            stack.push(float(token))

        # variabel
        elif token.isalpha():
            stack.push(float(variables[token]))

        # operator
        else:

            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.push(a + b)

            elif token == '-':
                stack.push(a - b)

            elif token == '*':
                stack.push(a * b)

            elif token == '/':
                stack.push(a / b)

            elif token == '^':
                stack.push(a ** b)

    return stack.pop()


# =========================
# BUILD EXPRESSION TREE
# =========================
def build_expression_tree(postfix):

    stack = Stack()

    operators = ['+', '-', '*', '/', '^']

    for token in postfix:

        node = TreeNode(token)

        if token in operators:

            node.right = stack.pop()
            node.left = stack.pop()

        stack.push(node)

    return stack.pop()


# =========================
# TRAVERSAL
# =========================
def inorder(node):

    if node:
        if node.left:
            print("(", end=" ")

        inorder(node.left)

        print(node.value, end=" ")

        inorder(node.right)

        if node.right:
            print(")", end=" ")


def preorder(node):

    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)


def postorder(node):

    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")


# =========================
# MAIN PROGRAM
# =========================
print("Perintah:")
print("SET <var> <nilai>")
print("DEFINE <ekspresi>")
print("EVAL <ekspresi>")
print("TREE <ekspresi>")
print("EXIT")
print()

while True:

    command = input(">> ")

    if command.upper() == "EXIT":
        break

    parts = command.split()

    # =====================
    # SET
    # =====================
    if parts[0].upper() == "SET":

        var = parts[1]
        value = float(parts[2])

        variables[var] = value

        print(f"Variabel {var} = {value}")

    # =====================
    # DEFINE
    # =====================
    elif parts[0].upper() == "DEFINE":

        defined_expression = " ".join(parts[1:])

        print("Ekspresi disimpan.")

    # =====================
    # EVAL
    # =====================
    elif parts[0].upper() == "EVAL":

        expression = " ".join(parts[1:])

        postfix = infix_to_postfix(expression)

        result = evaluate_postfix(postfix)

        print("Postfix =", " ".join(postfix))
        print("Hasil =", result)

    # =====================
    # TREE
    # =====================
    elif parts[0].upper() == "TREE":

        expression = " ".join(parts[1:])

        postfix = infix_to_postfix(expression)

        root = build_expression_tree(postfix)

        print("Inorder  :", end=" ")
        inorder(root)

        print()

        print("Preorder :", end=" ")
        preorder(root)

        print()

        print("Postorder:", end=" ")
        postorder(root)

        print()

    else:
        print("Perintah tidak dikenali.")
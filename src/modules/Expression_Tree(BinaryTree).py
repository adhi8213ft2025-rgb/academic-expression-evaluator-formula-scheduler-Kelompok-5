from typing import Optional, List

# Contoh operator dan fungsi
PREC = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
FUNCS = {'sin', 'cos', 'sqrt', 'log'}

# Node Linked List untuk Stack
class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Stack Linked List
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

        value = self.top.data
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None


# Expression Tree Node
class ExprNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional['ExprNode'] = None
        self.right: Optional['ExprNode'] = None


# Build Expression Tree dari postfix
def build_expr_tree(postfix: List[str]) -> Optional[ExprNode]:
    stack = Stack()

    for tok in postfix:

        # Operand angka atau variabel
        if tok.replace('.', '', 1).isdigit() or (
            tok.isalpha() and tok not in FUNCS
        ):
            stack.push(ExprNode(tok))

        # Operator binary
        elif tok in PREC:
            node = ExprNode(tok)

            node.right = stack.pop()
            node.left = stack.pop()

            stack.push(node)

        # Fungsi unary
        elif tok in FUNCS:
            node = ExprNode(tok)

            node.right = stack.pop()

            stack.push(node)

    return stack.pop()


# Traversal inorder
def inorder(root):
    if root is None:
        return ""

    if root.value in PREC:
        return f"({inorder(root.left)} {root.value} {inorder(root.right)})"

    elif root.value in FUNCS:
        return f"{root.value}({inorder(root.right)})"

    return str(root.value)


# Contoh postfix
postfix = ['a', 'b', '+', 'c', '*']

root = build_expr_tree(postfix)

print("Hasil Inorder:", inorder(root))

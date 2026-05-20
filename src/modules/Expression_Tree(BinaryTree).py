from typing import Optional, List

# Konstanta
PREC = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
FUNCS = {'sin', 'cos', 'tan', 'log', 'sqrt'}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class ExprNode:
    def __init__(self, value):          # ← Fix: '_init_' → '__init__'
        self.value = value
        self.left: Optional['ExprNode'] = None
        self.right: Optional['ExprNode'] = None


def build_expr_tree(postfix: List[str]) -> Optional[ExprNode]:
    stack = Stack()

    for tok in postfix:
        if tok.replace('.', '', 1).isdigit() or (
            tok.isalpha() and tok not in FUNCS
        ):
            stack.push(ExprNode(tok))

        elif tok in PREC:
            node = ExprNode(tok)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.push(node)

        elif tok in FUNCS:
            node = ExprNode(tok)
            node.right = stack.pop()
            stack.push(node)

    return stack.pop()


# Fungsi bantu untuk print tree (opsional, untuk testing)
def print_tree(node: Optional[ExprNode], level: int = 0, prefix: str = "Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left or node.right:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")


# Contoh penggunaan
if __name__ == "__main__":
    # Contoh postfix dari: 3 + 4 * 2
    postfix1 = ["3", "4", "2", "*", "+"]
    tree1 = build_expr_tree(postfix1)
    print("Tree untuk '3 + 4 * 2':")
    print_tree(tree1)

    print()

    # Contoh postfix dari: sin(x) + 2
    postfix2 = ["x", "sin", "2", "+"]
    tree2 = build_expr_tree(postfix2)
    print("Tree untuk 'sin(x) + 2':")
    print_tree(tree2)
    # update

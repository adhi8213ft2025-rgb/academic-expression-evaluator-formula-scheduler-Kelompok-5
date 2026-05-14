import math
import time
from typing import Optional, Dict, List, Tuple

# ── Precedence & associativity ─────────────────────────────────────

PREC = {
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
    '^': 4
}

RASSOC = {'^'}  # right-associative operators

FUNCS = {
    'sin': math.sin,
    'cos': math.cos,
    'sqrt': math.sqrt,
    'log': math.log,
    'abs': abs
}

# ── Node Linked List ───────────────────────────────────────────────

class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['LLNode'] = None


# ── Stack berbasis Linked List ─────────────────────────────────────

class Stack:
    def __init__(self):
        self.top: Optional[LLNode] = None
        self._size = 0

    def push(self, data) -> None:
        """Big-O: O(1)."""
        node = LLNode(data)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        """Big-O: O(1)."""
        if not self.top:
            return None

        val = self.top.data
        self.top = self.top.next
        self._size -= 1
        return val

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self) -> bool:
        return self._size == 0


# ── Tokenizer ──────────────────────────────────────────────────────

def tokenize(expr: str) -> List[str]:

    tokens = []
    i = 0

    while i < len(expr):
        ch = expr[i]

        if ch.isspace():
            i += 1
            continue

        if ch.isdigit() or (
            ch == '.' and i + 1 < len(expr) and expr[i + 1].isdigit()
        ):
            j = i

            while j < len(expr) and (
                expr[j].isdigit() or expr[j] == '.'
            ):
                j += 1

            tokens.append(expr[i:j])
            i = j

        elif ch.isalpha():
            j = i

            while j < len(expr) and expr[j].isalpha():
                j += 1

            tokens.append(expr[i:j])
            i = j

        elif ch in '+-*/^()':
            tokens.append(ch)
            i += 1

        else:
            raise ValueError(f'Token tidak dikenal: {ch!r}')

    return tokens


# ── Shunting-Yard: infix → postfix ─────────────────────────────────

def infix_to_postfix(tokens: List[str]) -> List[str]:
    """
    Big-O:
    - Waktu: O(n)
    - Ruang: O(n)
    """

    output: List[str] = []
    op_stack = Stack()

    for tok in tokens:

        if tok.replace('.', '', 1).isdigit() or (
            tok.isalpha() and tok not in FUNCS
        ):
            output.append(tok)

        elif tok in FUNCS:
            op_stack.push(tok)

        elif tok in PREC:

            while (
                not op_stack.is_empty()
                and op_stack.peek() in PREC
                and (
                    (
                        tok not in RASSOC
                        and PREC[tok] <= PREC[op_stack.peek()]
                    )
                    or (
                        tok in RASSOC
                        and PREC[tok] < PREC[op_stack.peek()]
                    )
                )
            ):
                output.append(op_stack.pop())

            op_stack.push(tok)

        elif tok == '(':
            op_stack.push(tok)

        elif tok == ')':

            while (
                not op_stack.is_empty()
                and op_stack.peek() != '('
            ):
                output.append(op_stack.pop())

            op_stack.pop()

            if (
                not op_stack.is_empty()
                and op_stack.peek() in FUNCS
            ):
                output.append(op_stack.pop())

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return output


# ── Expression Tree ────────────────────────────────────────────────

class ExprNode:
    def __init__(self, value):
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


# ── Traversal Expression Tree ──────────────────────────────────────

def inorder_expr(root: Optional[ExprNode]) -> str:
    if root is None:
        return ""

    if root.value in PREC:
        return (
            f"({inorder_expr(root.left)} "
            f"{root.value} "
            f"{inorder_expr(root.right)})"
        )

    elif root.value in FUNCS:
        return f"{root.value}({inorder_expr(root.right)})"

    return str(root.value)


def preorder_expr(root: Optional[ExprNode]) -> List[str]:
    if root is None:
        return []

    return (
        [root.value]
        + preorder_expr(root.left)
        + preorder_expr(root.right)
    )


def postorder_expr(root: Optional[ExprNode]) -> List[str]:
    if root is None:
        return []

    return (
        postorder_expr(root.left)
        + postorder_expr(root.right)
        + [root.value]
    )


# ── Evaluasi Expression Tree ───────────────────────────────────────

def eval_tree(
    root: Optional[ExprNode],
    var_table: Dict[str, float]
) -> float:

    if root is None:
        return 0.0

    val = root.value

    if val.replace('.', '', 1).isdigit():
        return float(val)

    if val.isalpha() and val not in FUNCS:
        return var_table[val]

    if val in PREC:
        left = eval_tree(root.left, var_table)
        right = eval_tree(root.right, var_table)

        if val == '+':
            return left + right

        if val == '-':
            return left - right

        if val == '*':
            return left * right

        if val == '/':
            return left / right

        if val == '^':
            return left ** right

    if val in FUNCS:
        arg = eval_tree(root.right, var_table)
        return FUNCS[val](arg)

    raise ValueError("Node tidak valid")


# ── BST Tabel Variabel ─────────────────────────────────────────────

class VarBSTNode:
    def __init__(self, key: str, val: float):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class VarBST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key, val):
        if node is None:
            return VarBSTNode(key, val)

        if key < node.key:
            node.left = self._insert(node.left, key, val)

        elif key > node.key:
            node.right = self._insert(node.right, key, val)

        else:
            node.val = val

        return node

    def set(self, key: str, val: float):
        self.root = self._insert(self.root, key, val)

    def _search(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node.val

        if key < node.key:
            return self._search(node.left, key)

        return self._search(node.right, key)

    def get(self, key: str) -> Optional[float]:
        return self._search(self.root, key)

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.key, node.val))
            self._inorder(node.right, result)

    def list_all(self) -> List[Tuple[str, float]]:
        result = []
        self._inorder(self.root, result)
        return result


# ── Graph DAG Dependensi Formula ───────────────────────────────────

class FormulaDAG:
    def __init__(self):
        self.adj: Dict[str, List[str]] = {}
        self.formulas: Dict[str, str] = {}

    def define(
        self,
        nama: str,
        ekspresi: str,
        deps: List[str]
    ) -> None:

        self.adj[nama] = deps
        self.formulas[nama] = ekspresi

    def topological_sort(self) -> List[str]:

        visited = set()
        temp = set()
        result = []

        def dfs(node):

            if node in temp:
                raise ValueError("Siklus terdeteksi")

            if node not in visited:
                temp.add(node)

                for nei in self.adj.get(node, []):
                    dfs(nei)

                temp.remove(node)
                visited.add(node)
                result.append(node)

        for node in self.adj:
            dfs(node)

        return result[::-1]


# ── Contoh ekspresi uji ────────────────────────────────────────────

TEST_EXPRS = [
    ('(a + b) * c', {'a': 2.0, 'b': 3.0, 'c': 4.0}),
    ('a ^ 2 + b ^ 2', {'a': 3.0, 'b': 4.0}),
    ('sin(a) + cos(b)', {'a': 0.0, 'b': 0.0}),
    ('sqrt(a * a + b * b)', {'a': 3.0, 'b': 4.0}),
    ('(a + b) * (a - b)', {'a': 5.0, 'b': 3.0}),
    ('log(a) + sqrt(b)', {'a': math.e, 'b': 16.0}),
    ('a * b + b * c + c * a', {
        'a': 1.0,
        'b': 2.0,
        'c': 3.0
    }),
    ('(a + b) ^ 2', {'a': 2.0, 'b': 3.0}),
    ('abs(a - b) * c', {
        'a': 1.0,
        'b': 4.0,
        'c': 2.0
    }),
    ('a / (b + c)', {
        'a': 10.0,
        'b': 2.0,
        'c': 3.0
    }),
   
]


# ── Main CLI ───────────────────────────────────────────────────────

def main():

    var_bst = VarBST()
    formula_dag = FormulaDAG()
    history_stack = Stack()

    print("Academic Expression Evaluator")
    print("Ketik BANTUAN untuk daftar perintah\n")

    print(f"Menjalankan {len(TEST_EXPRS)} ekspresi uji...\n")

    for expr, vals in TEST_EXPRS:

        for k, v in vals.items():
            var_bst.set(k, v)

        tokens = tokenize(expr)
        postfix = infix_to_postfix(tokens)
        tree = build_expr_tree(postfix)

        result = eval_tree(tree, vals)

        print(f"Ekspresi : {expr}")
        print(f"Postfix  : {' '.join(postfix)}")
        print(f"Hasil    : {result}")
        print("-" * 40)

    print("\nSelesai.")


if __name__ == '__main__':
    main()
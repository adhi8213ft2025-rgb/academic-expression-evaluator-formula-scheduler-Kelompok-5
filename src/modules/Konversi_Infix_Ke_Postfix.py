from typing import List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.stack import Stack

# ── Konstanta ──────────────────────────────────────────
OPERATORS = {'+', '-', '*', '/', '^'}

FUNCS = {'sin', 'cos', 'tan', 'log', 'sqrt', 'abs'}  # ← tambahkan ini

PRECEDENCE = {
    '+': 1, '-': 1,
    '*': 2, '/': 2,
    '^': 3
}

# ── Fungsi Utama ───────────────────────────────────────
def infix_to_postfix(tokens: List[str]) -> List[str]:
    op_stack = Stack()
    output = []

    for tok in tokens:
        if tok in FUNCS:                        # fungsi matematika
            op_stack.push(tok)
        elif tok in OPERATORS:
            while (not op_stack.is_empty()
                   and op_stack.peek() in OPERATORS
                   and PRECEDENCE.get(op_stack.peek(), 0) >= PRECEDENCE.get(tok, 0)):
                output.append(op_stack.pop())
            op_stack.push(tok)
        elif tok == '(':
            op_stack.push(tok)
        elif tok == ')':
            while not op_stack.is_empty() and op_stack.peek() != '(':
                output.append(op_stack.pop())
            op_stack.pop()  # buang '('
            if not op_stack.is_empty() and op_stack.peek() in FUNCS:
                output.append(op_stack.pop())
        else:
            output.append(tok)  # angka / variabel

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return output

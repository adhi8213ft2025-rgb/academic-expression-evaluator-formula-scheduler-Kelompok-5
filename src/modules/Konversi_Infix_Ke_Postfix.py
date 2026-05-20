from typing import List

<<<<<<< HEAD
from typing import List

=======
>>>>>>> ea9aeb999094f858a5404988975d10c62f6be204
# Prioritas operator
PREC = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

# Operator right-associative
RASSOC = {'^'}

# Tidak menggunakan fungsi sin, cos, dll
FUNCS = set()


# Implementasi Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def infix_to_postfix(tokens: List[str]) -> List[str]:
    """
    Mengubah ekspresi infix menjadi postfix

    Big-O:
    - Waktu: O(n)
    - Ruang: O(n)
    """

    output: List[str] = []
    op_stack = Stack()

    for tok in tokens:

        # Operand (angka atau variabel)
        if tok.replace('.', '', 1).isdigit() or tok.isalpha():
            output.append(tok)

        # Operator
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

        # Kurung buka
        elif tok == '(':
            op_stack.push(tok)

        # Kurung tutup
        elif tok == ')':

            while (
                not op_stack.is_empty()
                and op_stack.peek() != '('
            ):
                output.append(op_stack.pop())

            # Menghapus '('
            op_stack.pop()

    # Memindahkan sisa operator ke output
    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return output


# =========================
# Contoh penggunaan
# =========================

# Ekspresi: a + b * c
tokens = ['a', '+', 'b', '*', 'c']

hasil = infix_to_postfix(tokens)

print("Postfix:")
<<<<<<< HEAD
print(" ".join(hasil))
=======
print(" ".join(hasil))
>>>>>>> ea9aeb999094f858a5404988975d10c62f6be204

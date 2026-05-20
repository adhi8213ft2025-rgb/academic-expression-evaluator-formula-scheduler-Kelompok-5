# =========================================================
# benchmark.py
# Benchmark Struktur Data Stack
# Konversi Infix ke Postfix
# =========================================================

import time
import random


# =========================================================
# PRIORITAS OPERATOR
# =========================================================
PRIORITAS = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}


# =========================================================
# CLASS STACK
# =========================================================
class Stack:

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):

        if not self.is_empty():
            return self.data.pop()

        return None

    def peek(self):

        if not self.is_empty():
            return self.data[-1]

        return None

    def is_empty(self):
        return len(self.data) == 0


# =========================================================
# INFIX TO POSTFIX
# =========================================================
def infix_to_postfix(tokens):

    hasil = []

    stack = Stack()

    for token in tokens:

        # operand
        if token.isalpha() or token.isdigit():

            hasil.append(token)

        # kurung buka
        elif token == '(':

            stack.push(token)

        # kurung tutup
        elif token == ')':

            while (
                not stack.is_empty()
                and stack.peek() != '('
            ):

                hasil.append(stack.pop())

            stack.pop()

        # operator
        else:

            while (
                not stack.is_empty()
                and stack.peek() in PRIORITAS
                and PRIORITAS[token]
                <= PRIORITAS[stack.peek()]
            ):

                hasil.append(stack.pop())

            stack.push(token)

    # sisa operator
    while not stack.is_empty():

        hasil.append(stack.pop())

    return hasil


# =========================================================
# GENERATE RANDOM EXPRESSION
# =========================================================
def generate_expression(total_operand):

    operators = ['+', '-', '*', '/']

    tokens = []

    for i in range(total_operand):

        # operand random
        tokens.append(chr(random.randint(97, 122)))

        # operator
        if i < total_operand - 1:

            tokens.append(
                random.choice(operators)
            )

    return tokens


# =========================================================
# BENCHMARK
# =========================================================
def benchmark(total_operand):

    tokens = generate_expression(total_operand)

    print("\n===================================")
    print(" BENCHMARK INFIX TO POSTFIX")
    print("===================================")

    print(f"Jumlah Operand : {total_operand}")
    print(f"Jumlah Token   : {len(tokens)}")

    # mulai waktu
    start = time.perf_counter()

    postfix = infix_to_postfix(tokens)

    # akhir waktu
    end = time.perf_counter()

    print(f"Waktu Eksekusi : {end - start:.8f} detik")
    print(f"Jumlah Postfix : {len(postfix)}")


# =========================================================
# MAIN PROGRAM
# =========================================================
def main():

    ukuran_test = [
        100,
        1000,
        5000,
        10000,
        20000
    ]

    for ukuran in ukuran_test:

        benchmark(ukuran)


# =========================================================
# RUN PROGRAM
# =========================================================
if __name__ == "__main__":

    main()
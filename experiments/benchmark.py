import math
import timeit

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

def evaluate_postfix(postfix, variables, debug=False):
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

        # Trace stack hanya berjalan jika debug=True
        if debug:
            print(f"Token: {token}")
            print("Stack:", stack.to_list())
            print("-" * 30)

    return stack.pop()


# ── Script Driver & Benchmark ────────────────────

if __name__ == "__main__":
    print("=== UJI COBA FUNGSIONALITAS ===")
    
    # 1. Kasus Sederhana (a^2 + b^2)
    postfix1 = ['a', '2', '^', 'b', '2', '^', '+']
    vars1 = {'a': 3, 'b': 4}
    
    print("Menghitung ekspresi: a 2 ^ b 2 ^ +  dengan a=3, b=4")
    hasil1 = evaluate_postfix(postfix1, vars1, debug=True)
    print(f"Hasil Akhir Kasus 1: {hasil1}\n")

    # 2. Kasus Fungsi Matematika (sqrt(x) + sin(y))
    postfix2 = ['x', 'sqrt', 'y', 'sin', '+']
    vars2 = {'x': 9, 'y': math.pi / 2}
    
    print("Menghitung ekspresi: x sqrt y sin +  dengan x=9, y=pi/2")
    hasil2 = evaluate_postfix(postfix2, vars2, debug=False)
    print(f"Hasil Akhir Kasus 2: {hasil2}\n")


    print("=== MEMULAI BENCHMARK ===")
    print("Menguji kecepatan eksekusi sebanyak 100.000 kali running...")
    
    # Menyiapkan fungsi pembungkus tanpa print/debug agar benchmark akurat
    def run_benchmark():
        evaluate_postfix(postfix1, vars1, debug=False)

    # Menghitung total waktu eksekusi untuk 100.000 repetisi
    jumlah_iterasi = 100000
    total_waktu = timeit.timeit(run_benchmark, number=jumlah_iterasi)
    waktu_per_run = (total_waktu / jumlah_iterasi) * 1000000  # konversi ke mikrodetik

    print("-" * 40)
    print(f"Total waktu untuk {jumlah_iterasi:,} eksekusi : {total_waktu:.4f} detik")
    print(f"Rata-rata waktu per eksekusi             : {waktu_per_run:.2f} mikrodetik (µs)")
    print("-" * 40)
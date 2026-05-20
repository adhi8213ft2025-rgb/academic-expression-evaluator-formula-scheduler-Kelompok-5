# =========================================================
# queue_11.py
# Academic Expression Evaluator & Formula Scheduler
# Materi Struktur Data Queue (FIFO)
# =========================================================

from collections import deque
import math


# =========================================================
# CLASS FORMULA TASK
# =========================================================
class FormulaTask:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def __str__(self):
        return f"{self.name} = {self.expression}"


# =========================================================
# QUEUE IMPLEMENTATION
# =========================================================
class Queue:
    def __init__(self):
        self.items = deque()

    # ENQUEUE
    def enqueue(self, item):
        self.items.append(item)

    # DEQUEUE
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    # CHECK EMPTY
    def is_empty(self):
        return len(self.items) == 0

    # DISPLAY QUEUE
    def display(self):
        if self.is_empty():
            print("\nQueue kosong.")
        else:
            print("\n=== DAFTAR FORMULA DALAM QUEUE ===")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")

    # SIZE
    def size(self):
        return len(self.items)


# =========================================================
# EXPRESSION EVALUATOR
# =========================================================
class ExpressionEvaluator:

    @staticmethod
    def evaluate(expression):
        """
        Mengevaluasi ekspresi matematika sederhana.
        Mendukung:
        +, -, *, /, %, **
        sqrt(), sin(), cos(), tan(), log()
        """

        allowed_names = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "pi": math.pi,
            "e": math.e
        }

        try:
            result = eval(expression, {"__builtins__": None}, allowed_names)
            return result
        except Exception as e:
            return f"Error: {e}"


# =========================================================
# FORMULA SCHEDULER
# =========================================================
class FormulaScheduler:

    def __init__(self):
        self.queue = Queue()

    # TAMBAH FORMULA
    def add_formula(self, name, expression):
        task = FormulaTask(name, expression)
        self.queue.enqueue(task)
        print(f"\nFormula '{name}' berhasil ditambahkan ke queue.")

    # PROSES FORMULA FIFO
    def process_formula(self):

        if self.queue.is_empty():
            print("\nTidak ada formula dalam queue.")
            return

        task = self.queue.dequeue()

        print("\n================================")
        print(f"Memproses Formula : {task.name}")
        print(f"Ekspresi          : {task.expression}")

        result = ExpressionEvaluator.evaluate(task.expression)

        print(f"Hasil             : {result}")
        print("================================")

    # TAMPILKAN SEMUA FORMULA
    def show_formulas(self):
        self.queue.display()


# =========================================================
# MAIN PROGRAM
# =========================================================
def main():

    scheduler = FormulaScheduler()

    while True:

        print("\n========================================")
        print(" Academic Expression Evaluator")
        print(" Formula Scheduler - Queue FIFO")
        print("========================================")
        print("1. Tambah Formula")
        print("2. Proses Formula")
        print("3. Tampilkan Queue")
        print("4. Keluar")

        choice = input("\nPilih menu: ")

        # =====================================
        # TAMBAH FORMULA
        # =====================================
        if choice == "1":

            name = input("Nama Formula : ")
            expression = input("Ekspresi     : ")

            scheduler.add_formula(name, expression)

        # =====================================
        # PROSES FORMULA
        # =====================================
        elif choice == "2":

            scheduler.process_formula()

        # =====================================
        # TAMPILKAN QUEUE
        # =====================================
        elif choice == "3":

            scheduler.show_formulas()

        # =====================================
        # EXIT
        # =====================================
        elif choice == "4":

            print("\nProgram selesai.")
            break

        else:
            print("\nPilihan tidak valid.")


# =========================================================
# RUN PROGRAM
# =========================================================
if __name__ == "__main__":
    main()
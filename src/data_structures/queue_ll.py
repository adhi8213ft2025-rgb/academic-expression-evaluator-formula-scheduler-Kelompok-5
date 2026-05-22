# =========================================================
# queue_11.py
# Academic Expression Evaluator & Formula Scheduler
# Materi: Struktur Data Queue (FIFO)
# =========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    # =========================
    # ENQUEUE
    # =========================
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1
        print(f"[+] Formula '{data}' masuk ke scheduler.")

    # =========================
    # DEQUEUE
    # =========================
    def dequeue(self):
        if self.is_empty():
            print("[!] Queue kosong.")
            return None

        removed = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1

        print(f"[-] Formula '{removed}' diproses.")
        return removed

    # =========================
    # PEEK
    # =========================
    def peek(self):
        if self.is_empty():
            print("[!] Queue kosong.")
            return None

        return self.front.data

    # =========================
    # CHECK EMPTY
    # =========================
    def is_empty(self):
        return self.front is None

    # =========================
    # DISPLAY QUEUE
    # =========================
    def display(self):
        if self.is_empty():
            print("\n[ Queue Kosong ]")
            return

        current = self.front

        print("\n=== FORMULA SCHEDULER QUEUE ===")

        nomor = 1

        while current:
            print(f"{nomor}. {current.data}")
            current = current.next
            nomor += 1

        print("===============================\n")

    # =========================
    # TOTAL DATA
    # =========================
    def total_data(self):
        return self.size


# =========================================================
# MAIN PROGRAM
# =========================================================

def menu():
    print("==========================================")
    print(" Academic Expression Evaluator Scheduler ")
    print("==========================================")
    print("1. Tambah Formula ke Queue")
    print("2. Proses Formula")
    print("3. Lihat Antrian Formula")
    print("4. Formula Terdepan")
    print("5. Total Formula")
    print("0. Keluar")
    print("==========================================")


scheduler = Queue()

while True:
    menu()

    pilih = input("Pilih menu : ")

    # =====================================
    # TAMBAH FORMULA
    # =====================================
    if pilih == "1":
        formula = input("Masukkan formula : ")
        scheduler.enqueue(formula)

    # =====================================
    # PROSES FORMULA
    # =====================================
    elif pilih == "2":
        scheduler.dequeue()

    # =====================================
    # TAMPILKAN QUEUE
    # =====================================
    elif pilih == "3":
        scheduler.display()

    # =====================================
    # LIHAT DEPAN
    # =====================================
    elif pilih == "4":
        depan = scheduler.peek()

        if depan:
            print(f"\nFormula berikutnya : {depan}\n")

    # =====================================
    # TOTAL DATA
    # =====================================
    elif pilih == "5":
        print(f"\nTotal formula dalam queue : {scheduler.total_data()}\n")

    # =====================================
    # KELUAR
    # =====================================
    elif pilih == "0":
        print("\nProgram selesai.")
        break

    else:
        print("\n[!] Menu tidak valid.\n")

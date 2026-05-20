# Program Test Linked List Sederhana di Python

# Membuat Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Membuat Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan data di akhir
    def append(self, data):
        new_node = Node(data)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            return

        # Mencari node terakhir
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Menambahkan data di awal
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Menghapus node berdasarkan nilai
    def delete(self, key):
        current = self.head

        # Jika head yang dihapus
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None

        while current and current.data != key:
            prev = current
            current = current.next

        # Jika data tidak ditemukan
        if current is None:
            print("Data tidak ditemukan")
            return

        prev.next = current.next
        current = None

    # Menampilkan linked list
    def display(self):
        current = self.head

        if current is None:
            print("Linked List kosong")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# =========================
# TEST PROGRAM
# =========================

ll = LinkedList()

# Menambahkan data
ll.append(10)
ll.append(20)
ll.append(30)

print("Linked List setelah append:")
ll.display()

# Menambahkan di awal
ll.prepend(5)

print("\nLinked List setelah prepend:")
ll.display()

# Menghapus data
ll.delete(20)

print("\nLinked List setelah delete 20:")
ll.display()
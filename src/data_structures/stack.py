
from typing import Any, Optional

class Node:
    """Kelas untuk merepresentasikan satu node dalam Linked List."""
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional[Node] = None

class SinglyLinkedList:
    """Kelas Linked List sebagai fondasi penyimpanan Stack."""
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def add_front(self, data: Any) -> None:
        """Menambahkan elemen di depan (Top of Stack)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def remove_front(self) -> Any:
        """Menghapus elemen di depan dan mengembalikan nilainya."""
        if self.head is None:
            raise IndexError("List kosong")
        
        val = self.head.data
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            
        self.size -= 1
        return val

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) if nodes else "Empty"


class Stack:
    """Implementasi Stack yang aman dan bebas error."""
    def __init__(self):
        self._list = SinglyLinkedList()

    def push(self, data: Any) -> None:
        """Menambahkan data ke dalam stack."""
        self._list.add_front(data)

    def pop(self) -> Any:
        """Mengambil dan menghapus data teratas dari stack."""
        if self.is_empty():
            raise IndexError("Stack kosong")
        return self._list.remove_front()

    def peek(self) -> Any:
        """Melihat data teratas dari stack tanpa menghapusnya."""
        if self.is_empty():
            raise IndexError("Stack kosong")
        if self._list.head is not None:
            return self._list.head.data

    def is_empty(self) -> bool:
        """Memeriksa apakah stack kosong."""
        return len(self._list) == 0

    def __len__(self) -> int:
        """Mengembalikan jumlah elemen di dalam stack."""
        return len(self._list)

    def __repr__(self) -> str:
        """Representasi visual isi stack."""
        return f"Stack(top -> {self._list})"


# ==========================================
# CONTOH PENGUJIAN (Bisa langsung dijalankan)
# ==========================================
if __name__ == "__main__":
    print("--- Memulai Pengujian Stack ---")
    tumpukan = Stack()
    
    # 1. Uji push data
    tumpukan.push("Data_A")
    tumpukan.push("Data_B")
    tumpukan.push("Data_C")
    print("Isi awal:", tumpukan) 
    # Output: Stack(top -> Data_C -> Data_B -> Data_A)

    # 2. Uji peek data
    print("Data teratas saat ini (peek):", tumpukan.peek()) 
    # Output: Data_C

    # 3. Uji pop data
    print("Data yang dikeluarkan (pop):", tumpukan.pop()) 
    # Output: Data_C
    print("Isi setelah di-pop:", tumpukan) 
    # Output: Stack(top -> Data_B -> Data_A)

    # 4. Uji jumlah data
    print("Jumlah elemen:", len(tumpukan)) 
    # Output: 2
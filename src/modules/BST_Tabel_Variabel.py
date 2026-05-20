class Node:
    def __init__(self, key, value):
        self.key = key      # nama variabel
        self.value = value  # nilai variabel
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # INSERT / UPDATE
    def set(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value  # update nilai jika key sudah ada

        return node

    # GET VALUE
    def get(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # DELETE
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:
            # node dengan satu child / tanpa child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # node dengan dua child
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # LIST (INORDER)
    def list_variables(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.key, node.value))
            self._inorder(node.right, result)


# ==========================
# PROGRAM UTAMA
# ==========================

bst = BST()

while True:
    print("\n=== BST Tabel Variabel ===")
    print("1. SET variabel")
    print("2. GET variabel")
    print("3. DELETE variabel")
    print("4. LIST semua variabel")
    print("5. EXIT")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        key = input("Nama variabel: ")
        value = float(input("Nilai variabel: "))
        bst.set(key, value)
        print(f"Variabel '{key}' berhasil disimpan.")

    elif pilihan == "2":
        key = input("Nama variabel: ")
        value = bst.get(key)

        if value is not None:
            print(f"{key} = {value}")
        else:
            print("Variabel tidak ditemukan.")

    elif pilihan == "3":
        key = input("Nama variabel yang dihapus: ")
        bst.delete(key)
        print(f"Variabel '{key}' berhasil dihapus.")

    elif pilihan == "4":
        data = bst.list_variables()

        if not data:
            print("Tidak ada variabel.")
        else:
            print("\nDaftar Variabel (urut):")
            for k, v in data:
                print(f"{k} = {v}")

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
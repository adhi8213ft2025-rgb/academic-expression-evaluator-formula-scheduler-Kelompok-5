

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)

        return node

    # SEARCH
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False

        if data == node.data:
            return True

        if data < node.data:
            return self._search(node.left, data)

        return self._search(node.right, data)

    # DELETE
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete(node.left, data)

        elif data > node.data:
            node.right = self._delete(node.right, data)

        else:
            # Node tanpa child
            if node.left is None and node.right is None:
                return None

            # Node dengan satu child
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            # Node dengan dua child
            temp = self._min_value(node.right)

            node.data = temp.data

            node.right = self._delete(node.right, temp.data)

        return node

    # Cari node terkecil
    def _min_value(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    # INORDER TRAVERSAL
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=" ")
            self._inorder(node.right)


# =========================
# IMPLEMENTASI BST
# =========================

bst = BST()

# Insert data
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:")
bst.inorder()

# Search
print("Cari 40:", bst.search(40))
print("Cari 100:", bst.search(100))

# Delete
bst.delete(30)

print("Setelah delete 30:")
bst.inorder()
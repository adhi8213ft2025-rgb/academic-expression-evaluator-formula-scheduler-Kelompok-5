import unittest

# --- KODE BST MURNI KAMU ---
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


# --- KODE AUTOMATED UNIT TEST UNTUK BST ---
class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        """Inisialisasi BST baru dan data sampel sebelum setiap test."""
        self.bst = BST()
        self.sample_data = [50, 30, 70, 20, 40, 60, 80]
        for item in self.sample_data:
            self.bst.insert(item)

    def _get_inorder_list(self):
        """Helper untuk mengambil hasil inorder traversal sebagai Python List."""
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.data)
                traverse(node.right)
        traverse(self.bst.root)
        return result

    def test_insert_and_sorting(self):
        """Memastikan BST otomatis mengurutkan data secara asending (inorder)."""
        # Hasil penelusuran inorder dari BST harus selalu terurut secara numerik
        expected_sorted = [20, 30, 40, 50, 60, 70, 80]
        self.assertEqual(self._get_inorder_list(), expected_sorted)

    def test_tree_structure_properties(self):
        """Memastikan properti penempatan nilai kiri (lebih kecil) dan kanan (lebih besar) benar."""
        root = self.bst.root
        self.assertEqual(root.data, 50)
        
        # Sisi Kiri root harus lebih kecil dari 50
        self.assertEqual(root.left.data, 30)
        self.assertEqual(root.left.left.data, 20)
        self.assertEqual(root.left.right.data, 40)
        
        # Sisi Kanan root harus lebih besar dari 50
        self.assertEqual(root.right.data, 70)
        self.assertEqual(root.right.left.data, 60)
        self.assertEqual(root.right.right.data, 80)

    def test_search_exist_and_non_exist(self):
        """Memastikan fungsi pencarian mengembalikan True jika ada, dan False jika tidak ada."""
        # Test data yang ada di dalam tree
        self.assertTrue(self.bst.search(40))
        self.assertTrue(self.bst.search(50)) # Root
        self.assertTrue(self.bst.search(80))
        
        # Test data yang tidak ada di dalam tree
        self.assertFalse(self.bst.search(100))
        self.assertFalse(self.bst.search(10))

    def test_delete_leaf_node(self):
        """Kasus 1: Menghapus node yang tidak memiliki anak (leaf node)."""
        self.bst.delete(20)
        # 20 harus hilang, sisanya tetap terurut
        self.assertEqual(self._get_inorder_list(), [30, 40, 50, 60, 70, 80])
        self.assertFalse(self.bst.search(20))

    def test_delete_node_with_one_child(self):
        """Kasus 2: Menghapus node yang hanya memiliki satu anak (left/right)."""
        # Kita hapus dulu 20 agar node 30 hanya punya satu anak yaitu 40
        self.bst.delete(20)
        self.bst.delete(30) # Menghapus node 30 (memiliki 1 child yaitu 40)
        
        self.assertEqual(self._get_inorder_list(), [40, 50, 60, 70, 80])
        self.assertIsNone(self.bst.root.left.left) # Anak kiri 30 (20) sudah tidak ada
        self.assertEqual(self.bst.root.left.data, 40) # Posisi 30 digantikan oleh 40

    def test_delete_node_with_two_children(self):
        """Kasus 3: Menghapus node yang memiliki dua anak sekaligus."""
        # Menghapus node 30 (punya anak 20 dan 40)
        # Nilai 30 akan digantikan oleh nilai terkecil dari sub-tree kanan (Inorder Successor), yaitu 40
        self.bst.delete(30)
        
        self.assertEqual(self._get_inorder_list(), [20, 40, 50, 60, 70, 80])
        self.assertFalse(self.bst.search(30))
        self.assertEqual(self.bst.root.left.data, 40) # Nilai pengganti harus benar

    def test_delete_root(self):
        """Kasus Ekstrim: Menghapus root utama dari tree."""
        self.bst.delete(50) # Hapus 50 (Root)
        
        # Inorder harus tetap berurutan tanpa angka 50
        self.assertEqual(self._get_inorder_list(), [20, 30, 40, 60, 70, 80])
        # Root baru harus diambil dari elemen terkecil di kanan (60)
        self.assertEqual(self.bst.root.data, 60)


if __name__ == "__main__":
    print("\n=== MENJALANKAN AUTOMATED UNIT TEST BST ===")
    unittest.main()
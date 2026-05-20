import unittest

class Edge:
    def __init__(self, destination):
        self.destination = destination  # Menunjuk ke objek Vertex tujuan
        self.next_edge = None           # Pointer ke edge berikutnya (seperti Linked List)

class Vertex:
    def __init__(self, value):
        self.value = value
        self.head_edge = None           # Pointer ke simpul edge pertama yang terhubung
        self.next_vertex = None         # Pointer ke vertex berikutnya dalam Graph

class PureGraph:
    def __init__(self):
        self.head_vertex = None         # Pointer utama ke vertex pertama di dalam graph

    def add_vertex(self, value):
        """Menambahkan simpul baru ke dalam graph (O(1))"""
        new_vertex = Vertex(value)
        new_vertex.next_vertex = self.head_vertex
        self.head_vertex = new_vertex
        return new_vertex

    def find_vertex(self, value):
        """Mencari objek vertex berdasarkan nilainya"""
        current = self.head_vertex
        while current:
            if current.value == value:
                return current
            current = current.next_vertex
        return None

    def add_edge(self, source_value, dest_value, bidirectional=True):
        """Menambahkan hubungan antar simpul (O(1))"""
        source = self.find_vertex(source_value)
        dest = self.find_vertex(dest_value)

        if not source: source = self.add_vertex(source_value)
        if not dest: dest = self.add_vertex(dest_value)

        new_edge1 = Edge(dest)
        new_edge1.next_edge = source.head_edge
        source.head_edge = new_edge1

        if bidirectional:
            new_edge2 = Edge(source)
            new_edge2.next_edge = dest.head_edge
            dest.head_edge = new_edge2

    def display(self):
        """Menampilkan graph dengan menelusuri pointer murni"""
        current_vertex = self.head_vertex
        while current_vertex:
            print(f"Vertex {current_vertex.value} terhubung ke: ", end="")
            current_edge = current_vertex.head_edge
            neighbors = []
            while current_edge:
                neighbors.append(str(current_edge.destination.value))
                current_edge = current_edge.next_edge
            print(" -> ".join(neighbors) if neighbors else "Tidak ada")
            current_vertex = current_vertex.next_vertex


# --- KODE TEST UNTUK PURE GRAPH ---
class TestPureGraph(unittest.TestCase):

    def setUp(self):
        """Inisialisasi graph baru sebelum setiap fungsi test dijalankan."""
        self.graph = PureGraph()

    def _get_all_vertices(self):
        """Helper untuk mengambil semua value vertex sebagai Python list."""
        vertices = []
        current = self.graph.head_vertex
        while current:
            vertices.append(current.value)
            current = current.next_vertex
        return vertices

    def _get_neighbors(self, vertex_value):
        """Helper untuk mengambil semua value tetangga dari suatu vertex."""
        vertex = self.graph.find_vertex(vertex_value)
        if not vertex:
            return None
        
        neighbors = []
        current_edge = vertex.head_edge
        while current_edge:
            neighbors.append(current_edge.destination.value)
            current_edge = current_edge.next_edge
        return neighbors

    def test_add_vertex_and_find(self):
        """Memastikan vertex berhasil ditambahkan di depan (LIFO/O(1))."""
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')

        # Karena disisipkan di depan (head), urutannya harus ['B', 'A']
        self.assertEqual(self._get_all_vertices(), ['B', 'A'])

        # Memastikan pencarian vertex bekerja
        vertex_a = self.graph.find_vertex('A')
        self.assertIsNotNone(vertex_a)
        self.assertEqual(vertex_a.value, 'A')

        # Memastikan mencari vertex yang tidak ada mengembalikan None
        self.assertIsNone(self.graph.find_vertex('Z'))

    def test_add_edge_bidirectional(self):
        """Memastikan hubungan dua arah (bidirectional) terbentuk dengan benar."""
        self.graph.add_edge('A', 'B', bidirectional=True)

        # Cek tetangga A (harus ada B) dan tetangga B (harus ada A)
        self.assertIn('B', self._get_neighbors('A'))
        self.assertIn('A', self._get_neighbors('B'))

    def test_add_edge_unidirectional(self):
        """Memastikan hubungan satu arah bekerja (A -> B saja)."""
        # Set bidirectional=False untuk satu arah
        self.graph.add_edge('A', 'B', bidirectional=False)

        # A harus terhubung ke B
        self.assertIn('B', self._get_neighbors('A'))
        # Tapi B TIDAK boleh terhubung kembali ke A
        self.assertNotIn('A', self._get_neighbors('B'))

    def test_edge_lifo_order(self):
        """Memastikan edge baru selalu masuk di depan untaian head_edge (O(1))."""
        self.graph.add_edge('A', 'B', bidirectional=False)
        self.graph.add_edge('A', 'C', bidirectional=False)

        # Karena disisipkan di depan, tetangga terdekat dari head_edge harus 'C' baru kemudian 'B'
        self.assertEqual(self._get_neighbors('A'), ['C', 'B'])


if __name__ == "__main__":
    print("\n=== MENJALANKAN AUTOMATED UNIT TEST ===")
    unittest.main()
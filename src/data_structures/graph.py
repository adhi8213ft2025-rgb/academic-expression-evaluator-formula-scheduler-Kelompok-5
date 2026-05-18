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
        # Sisipkan di depan (head) agar kompleksitasnya O(1)
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
        # Cari atau buat vertex asal dan tujuan
        source = self.find_vertex(source_value)
        dest = self.find_vertex(dest_value)

        if not source: source = self.add_vertex(source_value)
        if not dest: dest = self.add_vertex(dest_value)

        # Hubungkan source -> dest
        new_edge1 = Edge(dest)
        new_edge1.next_edge = source.head_edge
        source.head_edge = new_edge1

        # Jika graph tidak berarah, hubungkan dest -> source
        if bidirectional:
            new_edge2 = Edge(source)
            new_edge2.next_edge = dest.head_edge
            dest.head_edge = new_edge2

    def display(self):
        """Menampilkan graph dengan menelusuri pointer murni"""
        current_vertex = self.head_vertex
        while current_vertex:
            print(f"Vertex {current_vertex.value} terhubung ke: ", end="")
            
            # Telusuri linked list dari edge
            current_edge = current_vertex.head_edge
            neighbors = []
            while current_edge:
                neighbors.append(str(current_edge.destination.value))
                current_edge = current_edge.next_edge
                
            print(" -> ".join(neighbors) if neighbors else "Tidak ada")
            current_vertex = current_vertex.next_vertex


# --- DEMO PENGGUNAAN GRAPH MURNI ---
print("=== IMPLEMENTASI GRAPH MURNI ===")
graph = PureGraph()

# Menambahkan hubungan antar vertex
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')

# Cetak hasilnya
graph.display()
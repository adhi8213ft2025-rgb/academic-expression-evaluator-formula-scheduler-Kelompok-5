# =========================================================
# FormulaDAG - Topological Sort & Cycle Detection
# Studi Kasus:
# F1 = a + b
# F2 = F1 * c
# F3 = F2 / F1
# F4 = F3 + F2
# =========================================================

class FormulaDAG:

    def __init__(self):
        # Dictionary graph
        self.graph = {}

    # -----------------------------------------------------
    # Menambahkan dependency formula
    # formula -> dependency
    # -----------------------------------------------------
    def add_dependency(self, formula, dependency):

        if formula not in self.graph:
            self.graph[formula] = []

        if dependency not in self.graph:
            self.graph[dependency] = []

        self.graph[formula].append(dependency)

    # -----------------------------------------------------
    # Menampilkan graph
    # -----------------------------------------------------
    def show_graph(self):

        print("\n=== DAG Formula ===")

        for formula in self.graph:
            print(f"{formula} -> {self.graph[formula]}")

    # -----------------------------------------------------
    # Topological Sort
    # -----------------------------------------------------
    def topological_sort(self):

        visited = set()
        visiting = set()
        stack = []

        for node in self.graph:

            if node not in visited:

                if not self._dfs(node, visited, visiting, stack):

                    print("\nTerdeteksi siklus!")
                    print("Formula tidak valid.\n")
                    return

        print("\n=== Urutan Evaluasi Formula ===")
        print(" -> ".join(stack[::-1]))

    # -----------------------------------------------------
    # DFS Recursive
    # -----------------------------------------------------
    def _dfs(self, node, visited, visiting, stack):

        # Deteksi siklus
        if node in visiting:
            return False

        # Jika sudah dikunjungi
        if node in visited:
            return True

        # Tandai sedang dikunjungi
        visiting.add(node)

        # Kunjungi dependency
        for neighbor in self.graph[node]:

            if not self._dfs(neighbor, visited, visiting, stack):
                return False

        # Selesai diproses
        visiting.remove(node)
        visited.add(node)

        # Masukkan ke stack
        stack.append(node)

        return True


# =========================================================
# IMPLEMENTASI FORMULA DAG
# =========================================================

dag = FormulaDAG()

# ---------------------------------------------------------
# Definisi Formula
# ---------------------------------------------------------
# F1 = a + b
# F2 = F1 * c
# F3 = F2 / F1
# F4 = F3 + F2
# ---------------------------------------------------------

# Dependency Formula
dag.add_dependency("F2", "F1")
dag.add_dependency("F3", "F2")
dag.add_dependency("F3", "F1")
dag.add_dependency("F4", "F3")
dag.add_dependency("F4", "F2")

# ---------------------------------------------------------
# Tampilkan Graph
# ---------------------------------------------------------
dag.show_graph()

# ---------------------------------------------------------
# Jalankan Topological Sort
# ---------------------------------------------------------
dag.topological_sort()


# =========================================================
# CONTOH SIKLUS
# =========================================================

print("\n==============================")
print("CONTOH GRAPH BERSIKLUS")
print("==============================")

cycle_dag = FormulaDAG()

cycle_dag.add_dependency("F1", "F2")
cycle_dag.add_dependency("F2", "F3")
cycle_dag.add_dependency("F3", "F1")

cycle_dag.show_graph()

cycle_dag.topological_sort()
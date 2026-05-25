class Graph:
    def __init__(self):
        self.graph = {}

    # Tambah edge A -> B
    def add_dependency(self, formula, dependency):
        if formula not in self.graph:
            self.graph[formula] = []

        if dependency not in self.graph:
            self.graph[dependency] = []

        self.graph[formula].append(dependency)

    # Topological Sort + Deteksi Siklus
    def topological_sort(self):
        visited = set()
        visiting = set()
        stack = []

        for node in self.graph:
            if node not in visited:
                if not self._dfs(node, visited, visiting, stack):
                    print("Terdeteksi siklus! Formula tidak valid.")
                    return

        print("Urutan evaluasi formula:")
        print(stack[::-1])

    # DFS
    def _dfs(self, node, visited, visiting, stack):

        # Deteksi siklus
        if node in visiting:
            return False

        if node in visited:
            return True

        visiting.add(node)

        for neighbor in self.graph[node]:
            if not self._dfs(neighbor, visited, visiting, stack):
                return False

        visiting.remove(node)
        visited.add(node)

        stack.append(node)

        return True


# ==========================
# IMPLEMENTASI DAG
# ==========================

g = Graph()

# A bergantung pada B dan C
g.add_dependency("A", "B")
g.add_dependency("A", "C")

# B bergantung pada D
g.add_dependency("B", "D")

# C bergantung pada D
g.add_dependency("C", "D")

# D tidak punya dependency

g.topological_sort()

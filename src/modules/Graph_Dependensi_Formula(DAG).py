# =========================================================
# Graph_Dependensi_Formula.py
# Directed Acyclic Graph (DAG)
# Academic Formula Dependency Graph
# =========================================================

from collections import defaultdict, deque


# =========================================================
# CLASS DAG
# =========================================================
class FormulaDAG:

    def __init__(self):

        # adjacency list
        self.graph = defaultdict(list)

        # menyimpan semua node formula
        self.nodes = set()

    # =====================================================
    # TAMBAH DEPENDENSI
    # Formula_A -> Formula_B
    # artinya B bergantung pada A
    # =====================================================
    def add_dependency(self, formula_a, formula_b):

        self.graph[formula_a].append(formula_b)

        self.nodes.add(formula_a)
        self.nodes.add(formula_b)

    # =====================================================
    # TAMPILKAN GRAPH
    # =====================================================
    def display_graph(self):

        print("\n===== GRAPH DEPENDENSI FORMULA =====")

        for node in self.nodes:

            if self.graph[node]:
                print(f"{node} --> {self.graph[node]}")
            else:
                print(f"{node} --> []")

    # =====================================================
    # DETEKSI SIKLUS (DFS)
    # =====================================================
    def has_cycle(self):

        visited = set()
        recursion_stack = set()

        # DFS RECURSIVE
        def dfs(node):

            visited.add(node)
            recursion_stack.add(node)

            for neighbor in self.graph[node]:

                # jika belum dikunjungi
                if neighbor not in visited:

                    if dfs(neighbor):
                        return True

                # jika ada di recursion stack
                elif neighbor in recursion_stack:
                    return True

            recursion_stack.remove(node)

            return False

        # cek semua node
        for node in self.nodes:

            if node not in visited:

                if dfs(node):
                    return True

        return False

    # =====================================================
    # TOPOLOGICAL SORT
    # KAHN'S ALGORITHM
    # =====================================================
    def topological_sort(self):

        # hitung indegree
        indegree = {node: 0 for node in self.nodes}

        for node in self.graph:

            for neighbor in self.graph[node]:

                indegree[neighbor] += 1

        # queue node dengan indegree 0
        queue = deque()

        for node in indegree:

            if indegree[node] == 0:
                queue.append(node)

        topo_order = []

        while queue:

            current = queue.popleft()

            topo_order.append(current)

            for neighbor in self.graph[current]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # jika jumlah node tidak sama
        # berarti ada siklus
        if len(topo_order) != len(self.nodes):

            print("\nGraph memiliki cyclic dependency.")
            return None

        return topo_order


# =========================================================
# MAIN PROGRAM
# =========================================================
def main():

    dag = FormulaDAG()

    # =====================================================
    # CONTOH FORMULA
    # =====================================================
    #
    # F1 = a + b
    # F2 = F1 * c
    # F3 = F2 / F1
    # F4 = F3 + F2
    #
    # Dependensi:
    # F1 -> F2
    # F1 -> F3
    # F2 -> F3
    # F2 -> F4
    # F3 -> F4
    #
    # =====================================================

    dag.add_dependency("F1", "F2")
    dag.add_dependency("F1", "F3")
    dag.add_dependency("F2", "F3")
    dag.add_dependency("F2", "F4")
    dag.add_dependency("F3", "F4")

    # =====================================================
    # TAMPILKAN GRAPH
    # =====================================================
    dag.display_graph()

    # =====================================================
    # CEK SIKLUS
    # =====================================================
    if dag.has_cycle():

        print("\nTerdapat cyclic dependency.")

    else:

        print("\nTidak ada cyclic dependency.")

        # =================================================
        # TOPOLOGICAL SORT
        # =================================================
        result = dag.topological_sort()

        print("\nUrutan Evaluasi Formula:")
        print(" -> ".join(result))


# =========================================================
# RUN PROGRAM
# =========================================================
if __name__ == "__main__":
    main()
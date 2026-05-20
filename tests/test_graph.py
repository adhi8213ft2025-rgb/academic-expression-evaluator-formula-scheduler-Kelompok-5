# =========================================================
# test_graph.py
# Academic Expression Evaluator Formula Scheduler
# Pengujian Struktur Data Graph (DAG)
# =========================================================

import unittest
from collections import defaultdict, deque


# =========================================================
# GRAPH CLASS
# =========================================================
class FormulaGraph:

    def __init__(self):

        self.graph = defaultdict(list)

        self.nodes = set()

    # ==========================================
    # TAMBAH DEPENDENSI
    # ==========================================
    def add_dependency(self, formula_a, formula_b):

        # formula_b bergantung pada formula_a
        self.graph[formula_a].append(formula_b)

        self.nodes.add(formula_a)
        self.nodes.add(formula_b)

    # ==========================================
    # DETEKSI SIKLUS
    # ==========================================
    def has_cycle(self):

        visited = set()

        recursion_stack = set()

        def dfs(node):

            visited.add(node)

            recursion_stack.add(node)

            for neighbor in self.graph[node]:

                if neighbor not in visited:

                    if dfs(neighbor):
                        return True

                elif neighbor in recursion_stack:

                    return True

            recursion_stack.remove(node)

            return False

        for node in self.nodes:

            if node not in visited:

                if dfs(node):
                    return True

        return False

    # ==========================================
    # TOPOLOGICAL SORT
    # ==========================================
    def topological_sort(self):

        indegree = {
            node: 0
            for node in self.nodes
        }

        for node in self.graph:

            for neighbor in self.graph[node]:

                indegree[neighbor] += 1

        queue = deque()

        for node in indegree:

            if indegree[node] == 0:

                queue.append(node)

        result = []

        while queue:

            current = queue.popleft()

            result.append(current)

            for neighbor in self.graph[current]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:

                    queue.append(neighbor)

        if len(result) != len(self.nodes):

            return None

        return result


# =========================================================
# UNIT TEST
# =========================================================
class TestAcademicFormulaGraph(unittest.TestCase):

    # ==========================================
    # TEST ADD DEPENDENCY
    # ==========================================
    def test_add_dependency(self):

        graph = FormulaGraph()

        graph.add_dependency(
            "F1",
            "F2"
        )

        self.assertIn("F2", graph.graph["F1"])

    # ==========================================
    # TEST NODE STORAGE
    # ==========================================
    def test_nodes_exist(self):

        graph = FormulaGraph()

        graph.add_dependency(
            "F1",
            "F2"
        )

        self.assertIn("F1", graph.nodes)

        self.assertIn("F2", graph.nodes)

    # ==========================================
    # TEST NO CYCLE
    # ==========================================
    def test_no_cycle(self):

        graph = FormulaGraph()

        graph.add_dependency("F1", "F2")
        graph.add_dependency("F2", "F3")
        graph.add_dependency("F3", "F4")

        self.assertFalse(
            graph.has_cycle()
        )

    # ==========================================
    # TEST CYCLE DETECTION
    # ==========================================
    def test_cycle_detection(self):

        graph = FormulaGraph()

        graph.add_dependency("F1", "F2")
        graph.add_dependency("F2", "F3")
        graph.add_dependency("F3", "F1")

        self.assertTrue(
            graph.has_cycle()
        )

    # ==========================================
    # TEST TOPOLOGICAL SORT
    # ==========================================
    def test_topological_sort(self):

        graph = FormulaGraph()

        graph.add_dependency("F1", "F2")
        graph.add_dependency("F2", "F3")
        graph.add_dependency("F3", "F4")

        result = graph.topological_sort()

        self.assertEqual(
            result,
            ["F1", "F2", "F3", "F4"]
        )

    # ==========================================
    # TEST TOPOLOGICAL SORT FAIL
    # ==========================================
    def test_topological_sort_cycle(self):

        graph = FormulaGraph()

        graph.add_dependency("F1", "F2")
        graph.add_dependency("F2", "F3")
        graph.add_dependency("F3", "F1")

        result = graph.topological_sort()

        self.assertEqual(result, None)

    # ==========================================
    # TEST MULTIPLE DEPENDENCIES
    # ==========================================
    def test_multiple_dependencies(self):

        graph = FormulaGraph()

        graph.add_dependency("F1", "F3")
        graph.add_dependency("F2", "F3")

        result = graph.topological_sort()

        self.assertIn("F1", result)
        self.assertIn("F2", result)
        self.assertIn("F3", result)

    # ==========================================
    # TEST SINGLE NODE
    # ==========================================
    def test_single_node(self):

        graph = FormulaGraph()

        graph.add_dependency("F1", "F2")

        self.assertEqual(
            len(graph.nodes),
            2
        )

    # ==========================================
    # TEST EMPTY GRAPH
    # ==========================================
    def test_empty_graph(self):

        graph = FormulaGraph()

        self.assertFalse(
            graph.has_cycle()
        )

        self.assertEqual(
            graph.topological_sort(),
            []
        )


# =========================================================
# MAIN TEST
# =========================================================
if __name__ == "__main__":

<<<<<<< HEAD
    unittest.main()
=======
    unittest.main()
>>>>>>> 674001a50a912b3b1ddff3596ca9dc867759a03b

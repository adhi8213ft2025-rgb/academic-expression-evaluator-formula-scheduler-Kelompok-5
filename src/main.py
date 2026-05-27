"""
============================================================
  ACADEMIC EXPRESSION EVALUATOR & FORMULA SCHEDULER
  Kelompok 5 — main.py Terintegrasi
============================================================
  Menggabungkan semua komponen dari:
    src/data_structures/ → stack, linked_list, queue_ll, bst, graph
    src/modules/         → BST_Variabel, Infix→Postfix, Evaluasi
                           Expression Tree, DAG, CLI Kalkulator
============================================================
"""

import sys, os, math, types, importlib.util

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

MODULES_DIR     = os.path.join(SRC_DIR, "modules")
DATA_STRUCT_DIR = os.path.join(SRC_DIR, "data_structures")

# ─── Helper: patch file agar top-level code tidak jalan ────
def _import_class_only(alias, filepath, class_names, func_names=()):
    """
    Baca source file, ekstrak hanya definisi class/def yang dibutuhkan,
    lalu compile dan exec di namespace bersih.
    Ini menghindari eksekusi kode top-level (while True, input, dll).
    """
    with open(filepath, encoding="utf-8") as f:
        source = f.read()

    import ast, textwrap
    tree   = ast.parse(source)
    wanted = set(class_names) | set(func_names)

    # Kumpulkan hanya node class/function yang diminta
    new_body = []
    for node in tree.body:
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name in wanted:
                new_body.append(node)
        elif isinstance(node, (ast.ImportFrom, ast.Import, ast.Assign, ast.AugAssign, ast.AnnAssign)):
            new_body.append(node)   # bawa semua import

    new_tree = ast.Module(body=new_body, type_ignores=[])
    ast.fix_missing_locations(new_tree)
    code = compile(new_tree, filepath, "exec")

    ns = {}
    exec(code, ns)
    return ns


#  DATA STRUCTURES

# ── stack.py ───────────────────────────────────────────────
from data_structures.stack import Stack, SinglyLinkedList

# ── linked_list.py (top-level code) ───────────────────────
_ns = _import_class_only(
    "linked_list",
    os.path.join(DATA_STRUCT_DIR, "linked_list.py"),
    class_names=["Node", "LinkedList"]
)
LinkedList = _ns["LinkedList"]

# ── queue_ll.py ────────────────────────────────────────────
from data_structures.queue_ll import (
    Queue, FormulaTask, FormulaScheduler, ExpressionEvaluator
)

# ── bst.py (top-level code) ────────────────────────────────
_ns = _import_class_only(
    "bst",
    os.path.join(DATA_STRUCT_DIR, "bst.py"),
    class_names=["Node", "BST"]
)
BST_Umum = _ns["BST"]

# ── graph.py ───────────────────────────────────────────────
from data_structures.graph import PureGraph

# ══════════════════════════════════════════════════════════
#  MODULES
# ══════════════════════════════════════════════════════════

# ── BST_Tabel_Variabel.py (while True top-level) ──────────
_ns = _import_class_only(
    "bst_var",
    os.path.join(MODULES_DIR, "BST_Tabel_Variabel.py"),
    class_names=["Node", "BST"]
)
BST_Variabel = _ns["BST"]

# ── Konversi_Infix_Ke_Postfix.py (contoh top-level) ───────
_ns = _import_class_only(
    "infix",
    os.path.join(MODULES_DIR, "Konversi_Infix_Ke_Postfix.py"),
    class_names=["Stack"],
    func_names=["infix_to_postfix"]
)
infix_to_postfix = _ns["infix_to_postfix"]

# ── Evaluasi_Postfix.py (contoh top-level) ─────────────────
_ns = _import_class_only(
    "eval_postfix",
    os.path.join(MODULES_DIR, "Evaluasi_Postfix.py"),
    class_names=["LLNode", "Stack"],
    func_names=["evaluate_postfix"]
)
evaluate_postfix = _ns["evaluate_postfix"]

# ── Expression_Tree(BinaryTree).py ─────────────────────────
_ns = _import_class_only(
    "expr_tree",
    os.path.join(MODULES_DIR, "Expression_Tree(BinaryTree).py"),
    class_names=["Stack", "ExprNode"],
    func_names=["build_expr_tree", "print_tree"]
)
build_expr_tree = _ns["build_expr_tree"]
print_tree      = _ns["print_tree"]

# ── Graph_Dependensi_Formula(DAG).py (top-level g.topological_sort) ──
_ns = _import_class_only(
    "dag",
    os.path.join(MODULES_DIR, "Graph_Dependensi_Formula(DAG).py"),
    class_names=["Graph"]
)
GraphDAG = _ns["Graph"]

# ── CLI_Kalkulator.py ──────────────────────────────────────
from modules.CLI_Kalkulator import jalankan_kalkulator_cli

# ══════════════════════════════════════════════════════════
#  DEMO — DATA STRUCTURES
# ══════════════════════════════════════════════════════════

def demo_stack():
    print("\n┌─── DEMO: Stack (Linked List) ───┐")
    s = Stack()
    for item in ["Alpha", "Beta", "Gamma"]:
        s.push(item)
        print(f"  push({item!r:7s}) → {s}")
    print(f"  peek()        = {s.peek()}")
    print(f"  pop()         = {s.pop()}")
    print(f"  Setelah pop   → {s}")
    print(f"  Jumlah elemen : {len(s)}")


def demo_linked_list():
    print("\n┌─── DEMO: Singly Linked List ───┐")
    ll = LinkedList()
    for v in [10, 20, 30]:
        ll.append(v)
    print("  append(10,20,30) → ", end=""); ll.display()
    ll.prepend(5)
    print("  prepend(5)       → ", end=""); ll.display()
    ll.delete(20)
    print("  delete(20)       → ", end=""); ll.display()


def demo_queue():
    print("\n┌─── DEMO: Queue FIFO — Formula Scheduler ───┐")
    sched = FormulaScheduler()
    sched.add_formula("Luas Lingkaran", "pi * 5 ** 2")
    sched.add_formula("Pythagoras",     "sqrt(3**2 + 4**2)")
    sched.show_formulas()
    sched.process_formula()
    sched.process_formula()


def demo_bst_umum():
    print("\n┌─── DEMO: BST Umum (Integer) ───┐")
    bst = BST_Umum()
    for n in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(n)
    print("  Inorder : ", end=""); bst.inorder()
    print("  Cari 40 :", bst.search(40))
    print("  Cari 99 :", bst.search(99))
    bst.delete(30)
    print("  Hapus 30 →", end=" "); bst.inorder()


def demo_graph():
    print("\n┌─── DEMO: Pure Graph (Pointer-based) ───┐")
    g = PureGraph()
    for u, v in [("A","B"), ("A","C"), ("B","D"), ("C","D")]:
        g.add_edge(u, v, bidirectional=False)
    g.display()

# ══════════════════════════════════════════════════════════
#  DEMO — MODULES
# ══════════════════════════════════════════════════════════

def demo_bst_variabel():
    print("\n┌─── DEMO: BST Tabel Variabel ───┐")
    bst = BST_Variabel()
    bst.set("x", 3.0); bst.set("y", 4.0); bst.set("z", 7.5)
    print("  Semua variabel  :", bst.list_variables())
    print("  GET x           =", bst.get("x"))
    bst.delete("z")
    print("  Setelah hapus z :", bst.list_variables())

def demo_infix_postfix():
    print("\n┌─── DEMO: Konversi Infix → Postfix ───┐")
    contoh = [
        ["a", "+", "b", "*", "c"],
        ["(", "a", "+", "b", ")", "*", "(", "c", "-", "d", ")"],
        ["x", "^", "2", "+", "y", "^", "2"],
    ]
    for tokens in contoh:
        print(f"  Infix  : {' '.join(tokens)}")
        print(f"  Postfix: {' '.join(infix_to_postfix(tokens))}\n")

def demo_evaluasi_postfix():
    print("\n┌─── DEMO: Evaluasi Postfix ───┐")
    postfix   = ["a", "2", "^", "b", "2", "^", "+"]   # a²+b²
    variables = {"a": 3, "b": 4}
    print(f"  Postfix  : {' '.join(postfix)}")
    print(f"  Variabel : {variables}")
    print(f"  Hasil    : {evaluate_postfix(postfix, variables)}")

def demo_expression_tree():
    print("\n┌─── DEMO: Expression Tree ───┐")
    postfix = ["3", "4", "2", "*", "+"]   # 3 + 4*2
    tree    = build_expr_tree(postfix)
    print("  Input postfix : 3 4 2 * +  (≡ 3 + 4×2)")
    print("  Struktur tree :")
    print_tree(tree)

def demo_dag():
    print("\n┌─── DEMO: DAG — Dependensi Formula ───┐")
    g = GraphDAG()
    g.add_dependency("A", "B"); g.add_dependency("A", "C")
    g.add_dependency("B", "D"); g.add_dependency("C", "D")
    print("  Dependensi: A→B, A→C, B→D, C→D")
    g.topological_sort()

# ══════════════════════════════════════════════════════════0
#  RUNNER
# ══════════════════════════════════════════════════════════

def jalankan_semua_demo():
    print("\n" + "═"*52 + "\n  DATA STRUCTURES\n" + "═"*52)
    demo_stack(); demo_linked_list(); demo_queue()
    demo_bst_umum(); demo_graph()
    print("\n" + "═"*52 + "\n  MODULES\n" + "═"*52)
    demo_bst_variabel(); demo_infix_postfix()
    demo_evaluasi_postfix(); demo_expression_tree(); demo_dag()

# ══════════════════════════════════════════════════════════
#  MENU UTAMA
# ══════════════════════════════════════════════════════════

MENU = """
╔══════════════════════════════════════════════════════╗
║   ACADEMIC EXPRESSION EVALUATOR — Kelompok 5         ║
╠══════════════════════════════════════════════════════╣
║  [1]  Demo Semua Komponen                            ║
║  [2]  Demo Data Structures Saja                      ║
║  [3]  Demo Modules Saja                              ║
║  [4]  Kalkulator CLI Interaktif                      ║
║  [0]  Keluar                                         ║
╚══════════════════════════════════════════════════════╝"""

def main():
    print(MENU)
    while True:
        try:
            pilihan = input("Pilih menu [0-4]: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nTerimakasih & Sampai jumpa!"); sys.exit(0)

        if   pilihan == "1": jalankan_semua_demo()
        elif pilihan == "2":
            demo_stack(); demo_linked_list(); demo_queue()
            demo_bst_umum(); demo_graph()
        elif pilihan == "3":
            demo_bst_variabel(); demo_infix_postfix()
            demo_evaluasi_postfix(); demo_expression_tree(); demo_dag()
        elif pilihan == "4":
            print("\n  Ketik EXIT untuk kembali ke menu.\n")
            try:    jalankan_kalkulator_cli()
            except KeyboardInterrupt:
                print("\n  Kembali ke menu utama.")
        elif pilihan == "0":
            print("Terimakasih & Sampai jumpa!"); sys.exit(0)
        else:
            print("  ✗ Masukkan angka 0–4.")

        print(MENU)

if __name__ == "__main__":
    main()
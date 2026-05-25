<<<<<<< HEAD
# =========================================================
# test_queue_11.py
# Academic Expression Evaluator Formula Scheduler
# Pengujian Struktur Data Queue (FIFO)
# =========================================================

import unittest
from collections import deque
import math


# =========================================================
# QUEUE CLASS
# =========================================================
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# =========================================================
# FORMULA TASK
# =========================================================
class FormulaTask:
    def __init__(self, title, expression):
        self.title = title
        self.expression = expression

    def __str__(self):
        return f"{self.title} -> {self.expression}"


# =========================================================
# EXPRESSION EVALUATOR
# =========================================================
class ExpressionEvaluator:

    @staticmethod
    def calculate(expression):

        allowed = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "pi": math.pi
        }

        try:
            return eval(expression, {"__builtins__": None}, allowed)

        except Exception:
            return "Invalid Expression"


# =========================================================
# FORMULA SCHEDULER
# =========================================================
class FormulaScheduler:

    def __init__(self):
        self.queue = Queue()

    def add_task(self, title, expression):

        task = FormulaTask(title, expression)

        self.queue.enqueue(task)

    def process_task(self):

        if self.queue.is_empty():
            return None

        task = self.queue.dequeue()

        result = ExpressionEvaluator.calculate(task.expression)

        return {
            "title": task.title,
            "expression": task.expression,
            "result": result
        }


# =========================================================
# UNIT TEST
# =========================================================
class TestQueue11(unittest.TestCase):

    # =====================================
    # TEST QUEUE EMPTY
    # =====================================
    def test_queue_empty(self):

        q = Queue()

        self.assertTrue(q.is_empty())

    # =====================================
    # TEST ENQUEUE
    # =====================================
    def test_enqueue(self):

        q = Queue()

        q.enqueue(10)

        self.assertEqual(q.size(), 1)

    # =====================================
    # TEST DEQUEUE
    # =====================================
    def test_dequeue(self):

        q = Queue()

        q.enqueue(100)

        result = q.dequeue()

        self.assertEqual(result, 100)

    # =====================================
    # TEST FIFO
    # =====================================
    def test_fifo(self):

        q = Queue()

        q.enqueue("A")
        q.enqueue("B")
        q.enqueue("C")

        self.assertEqual(q.dequeue(), "A")
        self.assertEqual(q.dequeue(), "B")
        self.assertEqual(q.dequeue(), "C")

    # =====================================
    # TEST FORMULA TASK
    # =====================================
    def test_formula_task(self):

        task = FormulaTask(
            "Circle Area",
            "pi * 7**2"
        )

        self.assertEqual(task.title, "Circle Area")

    # =====================================
    # TEST ADDITION
    # =====================================
    def test_addition_expression(self):

        result = ExpressionEvaluator.calculate("5 + 3")

        self.assertEqual(result, 8)

    # =====================================
    # TEST MULTIPLICATION
    # =====================================
    def test_multiplication_expression(self):

        result = ExpressionEvaluator.calculate("4 * 5")

        self.assertEqual(result, 20)

    # =====================================
    # TEST POWER
    # =====================================
    def test_power_expression(self):

        result = ExpressionEvaluator.calculate("2**4")

        self.assertEqual(result, 16)

    # =====================================
    # TEST SQRT
    # =====================================
    def test_sqrt_expression(self):

        result = ExpressionEvaluator.calculate("sqrt(81)")

        self.assertEqual(result, 9)

    # =====================================
    # TEST SIN
    # =====================================
    def test_sin_expression(self):

        result = ExpressionEvaluator.calculate("sin(0)")

        self.assertEqual(result, 0)

    # =====================================
    # TEST INVALID EXPRESSION
    # =====================================
    def test_invalid_expression(self):

        result = ExpressionEvaluator.calculate("10 / 0")

        self.assertEqual(result, "Invalid Expression")

    # =====================================
    # TEST ADD TASK
    # =====================================
    def test_scheduler_add_task(self):

        scheduler = FormulaScheduler()

        scheduler.add_task(
            "Kinetic Energy",
            "0.5 * 10 * 4**2"
        )

        self.assertEqual(
            scheduler.queue.size(),
            1
        )

    # =====================================
    # TEST PROCESS TASK
    # =====================================
    def test_scheduler_process_task(self):

        scheduler = FormulaScheduler()

        scheduler.add_task(
            "Simple Math",
            "10 + 5"
        )

        result = scheduler.process_task()

        self.assertEqual(
            result["result"],
            15
        )

    # =====================================
    # TEST PROCESS EMPTY QUEUE
    # =====================================
    def test_process_empty_queue(self):

        scheduler = FormulaScheduler()

        result = scheduler.process_task()

        self.assertEqual(result, None)


# =========================================================
# MAIN TEST
# =========================================================
if __name__ == "__main__":

    unittest.main()
=======
from src.data_structures.queue_11 import (
    Queue,
    FormulaTask,
    ExpressionEvaluator,
    FormulaScheduler
)


# =========================================================
# TEST QUEUE
# =========================================================

def test_enqueue():
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)

    assert q.size() == 2


def test_dequeue():
    q = Queue()

    q.enqueue("A")
    q.enqueue("B")

    result = q.dequeue()

    assert result == "A"
    assert q.size() == 1


def test_is_empty():
    q = Queue()

    assert q.is_empty() is True

    q.enqueue(1)

    assert q.is_empty() is False


def test_dequeue_empty():
    q = Queue()

    result = q.dequeue()

    assert result is None


# =========================================================
# TEST FORMULA TASK
# =========================================================

def test_formula_task():
    task = FormulaTask("Luas", "5*5")

    assert task.name == "Luas"
    assert task.expression == "5*5"
    assert str(task) == "Luas = 5*5"


# =========================================================
# TEST EXPRESSION EVALUATOR
# =========================================================

def test_expression_addition():
    result = ExpressionEvaluator.evaluate("2 + 3")

    assert result == 5


def test_expression_multiplication():
    result = ExpressionEvaluator.evaluate("4 * 5")

    assert result == 20


def test_expression_sqrt():
    result = ExpressionEvaluator.evaluate("sqrt(25)")

    assert result == 5


def test_expression_sin():
    result = ExpressionEvaluator.evaluate("sin(0)")

    assert result == 0


def test_expression_invalid():
    result = ExpressionEvaluator.evaluate("5 / 0")

    assert "Error" in str(result)


# =========================================================
# TEST FORMULA SCHEDULER
# =========================================================

def test_add_formula():
    scheduler = FormulaScheduler()

    scheduler.add_formula("Penjumlahan", "2+3")

    assert scheduler.queue.size() == 1


def test_process_formula():
    scheduler = FormulaScheduler()

    scheduler.add_formula("Perkalian", "4*5")

    scheduler.process_formula()

    assert scheduler.queue.is_empty() is True
>>>>>>> 0b509e5ffd2857fb63efaccca14037c7d45b969f

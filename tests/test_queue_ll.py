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

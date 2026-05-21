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
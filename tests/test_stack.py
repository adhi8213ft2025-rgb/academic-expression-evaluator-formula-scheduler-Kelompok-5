from src.data_structures.stack import Stack


def test_push():
    """Test push pada stack."""
    s = Stack()

    s.push("Data_A")
    s.push("Data_B")

    assert len(s) == 2
    assert s.peek() == "Data_B"


def test_pop():
    """Test pop pada stack."""
    s = Stack()

    s.push("Data_X")
    s.push("Data_Y")

    hasil = s.pop()

    assert hasil == "Data_Y"
    assert len(s) == 1
    assert s.peek() == "Data_X"


def test_peek():
    """Test peek pada stack."""
    s = Stack()

    s.push(100)

    assert s.peek() == 100
    assert len(s) == 1


def test_is_empty():
    """Test kondisi stack kosong."""
    s = Stack()

    assert s.is_empty() is True

    s.push(1)

    assert s.is_empty() is False


def test_len():
    """Test jumlah elemen stack."""
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    assert len(s) == 3


def test_repr():
    """Test representasi visual stack."""
    s = Stack()

    s.push("A")
    s.push("B")

    assert str(s) == "Stack(top -> B -> A)"


def test_pop_empty_stack():
    """Test pop pada stack kosong."""
    s = Stack()

    try:
        s.pop()
        assert False
    except IndexError:
        assert True


def test_peek_empty_stack():
    """Test peek pada stack kosong."""
    s = Stack()

    try:
        s.peek()
        assert False
    except IndexError:
        assert True
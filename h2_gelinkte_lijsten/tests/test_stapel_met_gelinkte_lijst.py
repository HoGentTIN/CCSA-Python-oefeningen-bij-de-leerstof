import pytest
from h2_gelinkte_lijsten.stapel_met_gelinkte_lijst import StackList

# test is_empty, push, peek en pop
@pytest.mark.timeout(1)
def test_stacklist_basic_functions():
    s = StackList()
    assert s.is_empty() is True

    s.push("This")
    assert s.is_empty() is False
    assert s.peek() == "This"

    s.push("Is")
    s.push("A Test")
    assert s.peek() == "A Test"

    assert s.pop() == "A Test"
    assert s.pop() == "Is"
    assert s.is_empty() is False

    assert s.pop() == "This"
    assert s.is_empty() is True


@pytest.mark.timeout(1)
def test_lifo_order_with_integers():
    s = StackList()
    for x in [1, 2, 3, 4, 5]:
        s.push(x)
    # LIFO: 5 → 4 → 3 → 2 → 1
    for expected in [5, 4, 3, 2, 1]:
        assert s.pop() == expected
    assert s.is_empty() is True


@pytest.mark.timeout(1)
def test_peek_does_not_remove():
    s = StackList()
    s.push("X")
    s.push("Y")
    assert s.peek() == "Y"   # top blijft Y
    assert s.peek() == "Y"   # nog steeds Y
    assert s.pop() == "Y"
    assert s.peek() == "X"
    assert s.pop() == "X"
    assert s.is_empty() is True


@pytest.mark.timeout(2)
def test_large_sequence():
    s = StackList()
    n = 1000
    for i in range(n):
        s.push(i)
    assert s.peek() == n - 1
    assert s.pop() == n - 1
    assert s.pop() == n - 2
    # leegmaken
    for _ in range(n - 2):
        s.pop()
    assert s.is_empty() is True



import pytest

from h4_bomen.binaire_hoop_met_vaste_grootte import BinaryHeap

@pytest.mark.timeout(2)
def test_binary_heap_case_0():
    b = BinaryHeap()
    assert b.empty() is True

    b.insert_elem(3)
    assert b.empty() is False

    b.insert_elem(1)
    b.insert_elem(2)
    assert str(b) == "[1, 3, 2]"

    assert b.remove_min_elem() == 1
    assert str(b) == "[2, 3]"

    assert b.remove_min_elem() == 2
    assert b.remove_min_elem() == 3
    assert str(b) == "[]"
    assert b.empty() is True


@pytest.mark.timeout(2)
def test_binary_heap_case_1():
    b2 = BinaryHeap(max_size=20)
    for elem in [11, 13, 1, 15, 6, 5, 9, 16, 3, 10, 7, 4, 12, 14, 2]:
        b2.insert_elem(elem)

    assert str(b2) == "[1, 3, 2, 6, 7, 5, 4, 16, 15, 13, 10, 11, 12, 14, 9]"

    assert b2.remove_min_elem() == 1
    assert b2.remove_min_elem() == 2
    assert b2.remove_min_elem() == 3

    b2.insert_elem(2)
    assert str(b2) == "[2, 6, 4, 14, 7, 5, 9, 16, 15, 13, 10, 12, 11]"


@pytest.mark.timeout(8)
def test_binary_heap_case_2_large():
    import random

    n = 10000
    b4 = BinaryHeap(max_size=n)
    elems = list(range(n))
    random.shuffle(elems)
    for e in elems:
        b4.insert_elem(e)

    assert b4.get_min_elem() == 0
    assert b4.remove_min_elem() == 0
    assert b4.get_min_elem() == 1

    # remove all but one
    for _ in range(n - 2):
        _ = b4.remove_min_elem()

    assert b4.get_min_elem() == n - 1

@pytest.mark.timeout(1)
def test_single_element_insert_and_remove():
    b = BinaryHeap()
    b.insert_elem(42)
    assert b.empty() is False
    assert b.get_min_elem() == 42
    assert b.remove_min_elem() == 42
    assert b.empty() is True
    assert str(b) == "[]"
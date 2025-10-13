import pytest

from h2_gelinkte_lijsten.wachtrij_met_gelinkte_lijst import QueueList


@pytest.mark.timeout(5)
def test_queuelist_basisfuncties():
    q = QueueList()
    assert q.is_empty() is True

    q.enqueue("One")
    assert q.is_empty() is False
    assert q.front() == "One"

    q.enqueue("Two")
    q.enqueue("Three")
    assert q.front() == "One"

    assert q.dequeue() == "One"
    assert q.dequeue() == "Two"
    assert q.front() == "Three"
    assert q.is_empty() is False

    q.enqueue("Four")
    assert q.dequeue() == "Three"
    assert q.dequeue() == "Four"
    assert q.is_empty() is True


@pytest.mark.timeout(5)
def test_queuelist_invert():
    q = QueueList()
    for x in range(1, 5):
        q.enqueue(x)

    assert q.front() == 1

    q.invert()
    assert q.front() == 4
    assert q.dequeue() == 4
    assert q.front() == 3

    q.invert()
    assert q.front() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.front() == 3

    q.invert()
    assert q.front() == 3
    assert q.dequeue() == 3

    q.invert()
    assert q.is_empty() is True

    q.enqueue(10)
    assert q.front() == 10

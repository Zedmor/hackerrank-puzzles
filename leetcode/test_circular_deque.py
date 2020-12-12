from pytest import fixture

from leetcode.design_circular_deque import MyCircularDeque


@fixture
def deque():
    return MyCircularDeque(3)


def test_empty(deque):
    assert deque.isEmpty() is True
    deque.insertLast(5)
    assert deque.isEmpty() is False


def test_full(deque):
    assert deque.isEmpty()
    assert deque.insertLast(1) is True
    assert deque.insertLast(2) is True
    assert deque.insertLast(3) is True

    assert deque.isFull()

    assert deque.insertLast(4) is False


def test_deletes(deque):
    assert deque.deleteLast() is False
    assert deque.deleteFront() is False
    deque.insertLast(1)
    assert deque.deleteLast() is True
    assert deque.deleteLast() is False
    deque.insertLast(1)
    assert deque.deleteFront() is True
    assert deque.deleteLast() is False


def test_gets(deque):
    assert deque.getRear() == -1
    assert deque.getFront() == -1
    assert deque.insertLast(1) is True
    assert deque.insertLast(2) is True
    assert deque.insertFront(3) is True
    assert deque.insertFront(4) is False
    assert deque.getRear() == 2
    assert deque.isFull() is True
    assert deque.deleteLast() is True
    assert deque.insertFront(4) is True
    assert deque.getFront() == 4

import pytest


def always1():
    return 1


def test_one():
    assert always1() == 1

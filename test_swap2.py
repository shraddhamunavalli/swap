from swap2 import swap_numbers

def test_case1():
    assert swap_numbers(5, 10) == "A : 10\nB : 5"

def test_case2():
    assert swap_numbers(0, 1) == "A : 1\nB : 0"

def test_case3():
    assert swap_numbers(-3, 7) == "A : 7\nB : -3"

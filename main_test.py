
from main import selection_sort
from random import randint

def test_selection_sort_normal_1():
    assert selection_sort([3, 2, 1]) == [1, 2, 3]

def test_selection_sort_normal_2():
    assert selection_sort([1, 7, 5, 3]) == [1, 3, 5, 7]

def test_selection_sort_one():
    assert selection_sort([1]) == [1]

def test_selection_sort_big():
    random_array = [randint(1, 100) for x in range(50)]
    assert selection_sort(random_array) == sorted(random_array)

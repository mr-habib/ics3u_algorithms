
from main import selection_sort
from random import randint

def test_selection_sort():
    assert selection_sort([3, 2, 1]) == [1, 2, 3]
    assert selection_sort([2, 4, 6]) == [2, 4, 6]
    random_array = [randint(1, 100) for x in range(50)]
    assert selection_sort(random_array) == sorted(random_array)

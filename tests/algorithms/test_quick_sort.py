from algorithms import quick_sort


def test_ascending_array(ascending_array):
    assert quick_sort(ascending_array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_descending_array(descending_array):
    assert quick_sort(descending_array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_identical_array(identical_array):
    assert quick_sort(identical_array) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def test_empty_array(empty_array):
    assert quick_sort(empty_array) == []

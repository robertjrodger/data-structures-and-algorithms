import pytest
from algorithms import binary_search


@pytest.fixture(scope="module")
def ordered_array():
    return [1, 3, 4, 7, 8, 9, 25]


@pytest.fixture(scope="module")
def identical_array():
    return [1, 1, 1, 1, 1, 1, 1]


def test_target_too_small(ordered_array):
    assert not binary_search(ordered_array, 0)


def test_target_too_big(ordered_array):
    assert not binary_search(ordered_array, 26)


def test_target_absent_but_in_range(ordered_array):
    assert not binary_search(ordered_array, 6)


def test_target_is_min(ordered_array):
    assert binary_search(ordered_array, 1)


def test_target_is_max(ordered_array):
    assert binary_search(ordered_array, 25)


def test_empty_array():
    assert not binary_search([], 5)


def test_target_present_array_size_one():
    assert binary_search([1], 1)


def test_target_absent_array_size_one():
    assert not binary_search([1], 2)


def test_target_present_array_size_two():
    assert binary_search([1, 2], 2)


def test_target_absent_array_size_two():
    assert not binary_search([1, 2], 3)


def test_target_present_array_identical(identical_array):
    assert binary_search(identical_array, 1)


def test_target_absent_array_identical(identical_array):
    assert not binary_search(identical_array, 2)

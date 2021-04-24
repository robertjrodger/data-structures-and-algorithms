import pytest


@pytest.fixture(scope="package")
def ascending_array():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture(scope="package")
def descending_array():
    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


@pytest.fixture(scope="package")
def identical_array():
    return [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


@pytest.fixture(scope="package")
def empty_array():
    return []

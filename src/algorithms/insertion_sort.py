"""
For each entry, swap with entries to the left until the entry to the left is smaller.

Time complexity:
    Best case: N-1 comparisons, no swaps --> O(N)
    Worst case: Initial order is decreasing, (1/2)N^2 comparisons and (1/2)N^2 exchanges
    If number of inversions (pairs of keys that are out-of-order) ~N, then sort runs in O(N)
"""

def insertion_sort(array):
    for idx in range(len(array)):
        move_back(array, idx)
    return array


def move_back(array, idx):
    while idx > 0:
        if left_is_smaller(array, idx):
            break
        else:
            exchange_with_left(array, idx)
            idx -= 1


def left_is_smaller(array, idx):
    return array[idx] > array[idx - 1]


def exchange_with_left(array, idx):
    array[idx], array[idx - 1] = array[idx - 1], array[idx]

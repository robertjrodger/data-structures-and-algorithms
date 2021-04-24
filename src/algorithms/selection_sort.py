"""
For each index, look to the right to see if any elements are less than the current element.
If so, swap the current element with the smallest element found to the right.

Time complexity:
    All cases: number of comparisons is 1 + 2 + 3 + ... + N = O(N^2)
"""
def selection_sort(array):
    for idx in range(len(array)):
        min_index = find_min_index_to_right(array, idx)
        if min_index != idx:
            exchange(array, idx, min_index)
    return array


def find_min_index_to_right(array, start_index):
    min_index = start_index
    current_min = array[start_index]
    for idx in range(start_index, len(array)):
        if array[idx] < current_min:
            min_index = idx
            current_min = array[idx]
    return min_index


def exchange(array, i, j):
    array[i], array[j] = array[j], array[i]

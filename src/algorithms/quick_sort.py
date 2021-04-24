from random import shuffle


"""
Pick a "pivot" element, sort the remaining items such that those smaller than the pivot are
to the left and those larger to the right, then put the pivot in between the two halves.
Recursively sort the left and right sides. Initial shuffle is to prevent worst-case scenario,
which is that the array is already sorted.

Time complexity:
    Best case: O(N ln N) (like merge sort, but generally faster because it involves fewer comparisons)
    Worst case: O(N^2) (happens when the array is already sorted in ascending or descending order, or when all elements are the same)

Possible improvements:
    + Switch to insertion sort when number of elements in half is ~10
    + Use three-way partitioning (maintaining a middle segment of elements equal to pivot value; can use Dijkstra's Dutch National Flag approach)
        + Randomized + three-way partitioning leads to linear-time sorting in broad class of applications!
"""
def quick_sort(array):
    shuffle(array)
    return sort(array)


def sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    i = 1
    j = len(array) - 1
    while i <= j:
        while i < len(array) and array[i] < pivot:
            i += 1
        while j >= 0 and array[j] > pivot:
            j -= 1
        if i < j:
            swap(array, i, j)
        else:
            break
    swap(array, 0, j)
    sorted_left = sort(array[:j].copy())
    sorted_right = sort(array[j + 1:].copy())
    return concat(sorted_left, array[j], sorted_right)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def concat(left: list, middle: int, right: list):
    concatenated = left
    concatenated.append(middle)
    concatenated.extend(right)
    return concatenated



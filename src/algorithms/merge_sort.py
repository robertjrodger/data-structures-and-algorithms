"""
Divide in half, recursively sort each half, merge the two halves.
Time complexity:
    Best and worst case: N ln N
Possible improvements:
    + Use insertion sort if a subarray has 7 or fewer elements (20% faster)
    + Check if biggest element in left subarray is smaller than smallest element in right subarray
        + If so, just concatenate
"""
def merge_sort(array):
    if len(array) < 2:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    else:
        middle_idx = len(array) // 2
        left = array[:middle_idx].copy()
        right = array[middle_idx:].copy()
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        return merge(sorted_left, sorted_right)


def merge(left, right):
    merged = []
    current_left_idx = 0
    current_right_idx = 0
    while current_left_idx < len(left) and current_right_idx < len(right):
        if left[current_left_idx] < right[current_right_idx]:
            merged.append(left[current_left_idx])
            current_left_idx += 1
        else:
            merged.append(right[current_right_idx])
            current_right_idx += 1
    if current_left_idx == len(left):
        merged.extend(right[current_right_idx:])
    else:
        merged.extend(left[current_left_idx:])
    return merged

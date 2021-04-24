"""
Input array must be sorted!
"""
def binary_search(array, target):
    if len(array) < 3:
        if target in array:
            return True
        else:
            return False

    mid = len(array) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array[:mid], target)
    else:
        return binary_search(array[mid:], target)

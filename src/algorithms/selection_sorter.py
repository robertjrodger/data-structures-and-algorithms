class SelectionSorter:
    """
    For each index, look to the right to see if any elements are less than the current element.
    If so, swap the current element with the smallest element found to the right.

    Time complexity:
        All cases: number of comparisons is 1 + 2 + 3 + ... + N = O(N^2)
    """
    @classmethod
    def sort(cls, array):
        num_items = len(array)
        for idx in range(0, num_items):
            min_index = cls._find_min_index(array, idx)
            if min_index != idx:
                cls._exchange(array, idx, min_index)
        return array

    @classmethod
    def _find_min_index(cls, array, start_index):
        min_index = start_index
        current_min = array[start_index]
        for idx in range(start_index, len(array)):
            if array[idx] < current_min:
                min_index = idx
                current_min = array[idx]
        return min_index

    @classmethod
    def _exchange(cls, array, i, j):
        array[i], array[j] = array[j], array[i]

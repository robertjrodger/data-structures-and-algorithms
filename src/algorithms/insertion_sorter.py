class InsertionSorter:
    """
    For each entry, swap with entries to the left until the entry to the left is smaller.

    Time complexity:
        Best case: N-1 comparisons, no swaps --> O(N)
        Worst case: Initial order is decreasing, (1/2)N^2 comparisons and (1/2)N^2 exchanges
        If number of inversions (pairs of keys that are out-of-order) ~N, then sort runs in O(N)
    """
    @classmethod
    def sort(cls, array):
        for idx in range(len(array)):
            cls._move_back(array, idx)
        return array

    @classmethod
    def _move_back(cls, array, idx):
        while idx > 0:
            if cls._left_is_smaller(array, idx):
                break
            else:
                cls._exchange_with_left(array, idx)
                idx -= 1

    @classmethod
    def _left_is_smaller(cls, array, idx):
        return array[idx] > array[idx - 1]

    @classmethod
    def _exchange_with_left(cls, array, idx):
        array[idx], array[idx - 1] = array[indx - 1], array[idx]

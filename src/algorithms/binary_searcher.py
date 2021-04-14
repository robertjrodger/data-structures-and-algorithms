class BinarySearcher:
    """
    Input array must be sorted!
    """
    @classmethod
    def search(cls, array, target):
        if len(array) < 3:
            if target in array:
                return True
            else:
                return False
        mid = len(array) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            return cls.search(array[:mid], target)
        else:
            return cls.search(array[mid:], target)

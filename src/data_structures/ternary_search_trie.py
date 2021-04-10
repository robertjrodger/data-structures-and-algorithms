OFFSET = 97


class Node:
    def __init__(self, char):
        self.char = char
        self.value: Optional[str] = None
        self.left: Optional[Node] = None
        self.middle: Optional[Node] = None
        self.right: Optional[Node] = None


class TernarySearchTrie:
    """
    Fast miss (faster than hashing). Supports ordered symbol table operations (rank, e.g.).

    Possible improvements:
        + initiate trie with all possible ALPHABET_SIZE^2 bigrams
        + use rebalancing
    """
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self._put(self.root, key, value, 0)

    def _put(self, current, key, value, current_idx):
        if current is None:
            current = Node(key[current_idx])
        next_idx = current_idx
        if current.char == key[current_idx]:
            if current_idx == len(key) - 1:
                current.value = value
                return current
            else:
                next_idx += 1
        next_char = key[next_idx]
        if next_char < current.char:
            current.left = self._put(current.left, key, value, next_idx)
        elif next_char == current.char:
            current.middle = self._put(current.middle, key, value, next_idx)
        else:
            current.right = self._put(current.right, key, value, next_idx)
        return current

    def get(self, key):
        return self._get(self.root, key, 0)

    def _get(self, current, key, current_idx):
        key_idx = len(key) - 1
        current_idx = 0
        while current:
            if current.char == key[current_idx]:
                if current_idx == key_idx:
                    return current.value
                else:
                    current_idx += 1
            next_char = key[current_idx]
            if next_char < current.char:
                current = current.left
            elif next_char == current.char:
                current = current.middle
            else:
                current = current.right
        return None

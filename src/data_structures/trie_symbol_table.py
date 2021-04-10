ALPHABET_SIZE = 26
OFFSET = 97


class Node:
    def __init__(self):
        self.value: Optional[str] = None
        self.next: list(Optional[Node]) = [None] * ALPHABET_SIZE


class TrieSymbolTable:
    """
    Trie-based symbol table for strings using the 26 lowercase ASCII letters.
    Root node never represents a key.

    Time complexity:
        search: O(length of string); miss complexity is typically sublinear in length of string
    Space complexity:
        ALPHABET_SIZE None links at each leaf; sublinear space possible if many short strings and/or
            many common prefixes
    """
    def __init__(self):
        self.root: Optional[Node] = None

    def _idx(self, char):
        return ord(char) - OFFSET

    def put(self, key, val):
        self.root = self._put(self.root, key, val, 0)

    def _put(self, current_node, key, val, next_key_idx):
        if current_node is None:
            current_node = Node()
        if next_key_idx == len(key):
            current_node.value = val
        else:
            next_char_idx = self._idx(key[next_key_idx])
            current_node.next[next_char_idx] = self._put(current_node.next[next_char_idx], key, val, next_key_idx + 1)
        return current_node

    def get(self, key):
        current = self.root
        final_idx = len(key)
        key_idx = 0
        while current:
            if key_idx == final_idx:
                return current.value
            else:
                char_idx = self._idx(key[key_idx])
                current = current.next[char_idx]
                key_idx += 1
        return None

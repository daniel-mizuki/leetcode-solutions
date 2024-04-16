class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node["end"] = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char not in current_node:
                return False
            current_node = current_node[char]
        if "end" not in current_node:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return True

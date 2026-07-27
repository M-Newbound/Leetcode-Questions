class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, word: str):
        node = self
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.searchPrefix(prefix) is not None


if __name__ == "__main__":
# Your Trie object will be instantiated and called as such:
  obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

print(obj.insert("apple"))
print(obj.search("apple"))   # 返回 True
print(obj.search("app"))     # 返回 False
print(obj.startsWith("app")) # 返回 True
print(obj.insert("app"))
print(obj.search("app"))     # 返回 True

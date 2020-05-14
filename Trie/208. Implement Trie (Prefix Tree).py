class trieNode:
    def __init__(self):
        self.children = collections.defaultdict(trieNode) 
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = trieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for i in word:
            current = current.children[i]
        current.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for i in word:
            current = current.children.get(i)
            if current == None:
                return False
        return current.isWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for i in prefix:
            current = current.children.get(i)
            if current == None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_tree = {}
        self.hash_set = set()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.hash_set.add(word)
        hash_tree = self.hash_tree
        for c in word:
            if c not in hash_tree.keys():
                hash_tree[c] = {}
            hash_tree = hash_tree[c]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.hash_set
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        hash_tree = self.hash_tree
        for c in prefix:
            hash_tree = hash_tree.get(c)
            if hash_tree is None:
                return False
        
        return True
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


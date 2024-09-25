class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.score += 1

    def getPrefixScore(self, word):
        cur = self.root
        total_score = 0
        for c in word:
            cur = cur.children[c]
            total_score += cur.score
        return total_score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = [trie.getPrefixScore(word) for word in words]
        return res

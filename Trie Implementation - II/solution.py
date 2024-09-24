class TrieNode:
    def __init__(self):
        self.children = {}
        self.endwith = 0
        self.countprefix = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.countprefix += 1
        cur.endwith += 1  
    def countWordsEqualTo(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0 
            cur = cur.children[c]
        return cur.endwith 
    def countWordsStartingWith(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.countprefix

    def erase(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return
            cur.children[c].countprefix -= 1
            if cur.children[c].countprefix == 0:
                del cur.children[c]
                return
            cur = cur.children[c]
        cur.endwith -= 1
        if cur.endwith < 0:
            cur.endwith = 0

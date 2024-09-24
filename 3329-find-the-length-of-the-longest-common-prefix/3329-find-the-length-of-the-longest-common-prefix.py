class TrieNode:
    def __init__(self):
        self.children={}
        self.endofword=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
    def lcp_length(self,word):
        cur=self.root
        leng=0
        for c in word:
            if c not in cur.children:
                return leng
            cur=cur.children[c]
            leng+=1
        return leng
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        maxi=0
        trie=Trie()
        for word in arr1:
            trie.insert(str(word))
        for word in arr2:
            maxi=max(maxi,trie.lcp_length(str(word)))
        return maxi
        
        
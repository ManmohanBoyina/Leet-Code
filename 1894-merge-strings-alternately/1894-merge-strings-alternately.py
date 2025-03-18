class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left,right=0,0
        res=''
        while left!=len(word1) and right!=len(word2):
            res+=word1[left]
            res+=word2[right]
            left+=1
            right+=1
        while left!=len(word1):
            res+=word1[left]
            left+=1
        while right!=len(word2):
            res+=word2[right]
            right+=1
        return res

        
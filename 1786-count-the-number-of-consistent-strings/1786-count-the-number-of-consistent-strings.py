class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=0
        for word in words:
            c=0
            for i in word:
                if i in allowed:
                    c+=1
            if c==len(word):
                res+=1
        return res
                
        
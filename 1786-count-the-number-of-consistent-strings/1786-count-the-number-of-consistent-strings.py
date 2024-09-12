class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=len(words)
        for word in words:
            for i in word:
                if i not in allowed:
                    res-=1
                    break
        return res
                
        
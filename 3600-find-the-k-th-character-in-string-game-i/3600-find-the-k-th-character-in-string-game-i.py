class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        def fstr(s, k):
            if len(s) >= k:
                return s[k-1]
            n = len(s)
            for i in range(n):
                s += chr(ord(s[i]) + 1)
            return fstr(s, k)
        return fstr(s, k)

        
        
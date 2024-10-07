class Solution:
    def minLength(self, s: str) -> int:
        l = 0
        s = list(s)
        while l < len(s) - 1:
            if (s[l] == 'A' and s[l + 1] == 'B') or (s[l] == 'C' and s[l + 1] == 'D'):
                del s[l:l + 2]
                if l > 0:
                    l -= 1
            else:
                l += 1
        return len(s)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def is_pali(l, r, s):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
            
        for r in reversed(range(len(s))):
            if is_pali(0, r, s):  # The string should be checked from 0 to r
                suffix = s[r+1:]  # Take the part after the palindrome
                return suffix[::-1] + s  # Reverse the suffix and prepend it to the original string
        return ""

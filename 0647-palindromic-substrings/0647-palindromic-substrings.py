class Solution:
    def countSubstrings(self, s: str) -> int:
        @lru_cache(None)
        def isPalindrome(left, right):
            if left > right: return True
            if s[left] != s[right]: return False
            return isPalindrome(left+1, right-1)
        
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):
                    ans += 1
        return ans
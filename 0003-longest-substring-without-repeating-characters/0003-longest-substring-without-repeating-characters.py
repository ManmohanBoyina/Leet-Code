class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        strr = ''
        ans = 0
        for right in range(len(s)):
            while s[right] in strr:
                strr = strr[1:]  # Remove the leftmost character from current substring
                left += 1
            strr += s[right]
            ans = max(ans, right - left + 1)
        return ans
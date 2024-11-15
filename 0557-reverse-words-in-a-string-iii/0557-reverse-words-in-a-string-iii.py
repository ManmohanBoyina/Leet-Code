class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, 0
        a = ""
        while right <= len(s):
            if right < len(s) and s[right] != " ":
                right += 1
            else:
                # Reverse the word from 'left' to 'right' and add to 'a'
                a += s[left:right][::-1] + " "
                right += 1
                left = right
        return a.strip()
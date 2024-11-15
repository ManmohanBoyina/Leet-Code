class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for right in range(len(word)):
            if word[right] == ch:
                return word[:right+1][::-1] + word[right+1:]
        return word
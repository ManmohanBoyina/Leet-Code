class Solution:
    def robotWithString(self, s: str) -> str:
        stack = []
        result = []
        min_suffix = [None] * len(s)
        min_char = 'z'
        for i in reversed(range(len(s))):
            min_char = min(min_char, s[i])
            min_suffix[i] = min_char
        for i, char in enumerate(s):
            stack.append(char)
            while stack and (i == len(s) - 1 or stack[-1] <= min_suffix[i + 1]):
                result.append(stack.pop())
        return ''.join(result)
from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        a = Counter(s)
        sorted_chars = sorted(a.keys(), key=lambda x: a[x], reverse=True)
        b = "".join(char * a[char] for char in sorted_chars)
        return b
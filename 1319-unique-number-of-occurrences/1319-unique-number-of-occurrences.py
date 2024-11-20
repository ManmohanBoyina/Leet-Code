from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a=Counter(arr)
        b=set(a.values())
        return len(a)==len(b)

        
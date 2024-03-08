from collections import Counter
class Solution(object):
    def maxFrequencyElements(self, nums):
        a = Counter(nums)
        max_value = max(a.values())
        c = 0
        for key, value in a.items():
            if value == max_value:
                c += max_value
        return c
        
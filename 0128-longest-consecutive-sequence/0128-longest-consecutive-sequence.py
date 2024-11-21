class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = sorted(set(nums))
        left = 0
        maxi = 1
        for right in range(1, len(a)):
            if a[right] != a[left] + (right - left):
                left = right
            maxi = max(maxi, right - left + 1)
        return maxi
from typing import List
from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        sum_, count = 0, 0
        for num in nums:
            sum_ += num
            if sum_ - goal in prefix_count:
                count += prefix_count[sum_ - goal]
            prefix_count[sum_] += 1
        return count

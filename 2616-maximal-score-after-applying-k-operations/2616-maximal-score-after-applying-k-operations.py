import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        a=[-x for x in nums]
        heapq.heapify(a)
        sum=0
        for i in range(k):
            b=-heapq.heappop(a)
            sum+=b
            heapq.heappush(a,-b//3)
        return sum
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=[-x for x in nums]
        heapq.heapify(a)
        for i in range(k-1):
            heapq.heappop(a)
        return -a[0]
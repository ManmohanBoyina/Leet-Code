class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        a=[]
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            if i>=k-1:
                while heap[0][1]<=i-k:
                    heapq.heappop(heap)
                a.append(-heap[0][0])
        return a
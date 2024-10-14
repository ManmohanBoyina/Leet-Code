import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a = [-x for x in stones]
        heapq.heapify(a)
        while len(a) > 1:
            a1 = -heapq.heappop(a)
            a2 = -heapq.heappop(a)
            if a1 != a2:
                heapq.heappush(a, -(a1 - a2))
        return -a[0] if a else 0
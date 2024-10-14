class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        for x,y in points:
            dist=math.sqrt((x**2)+(y**2))
            h.append([dist,x,y])
        heapq.heapify(h)
        res=[]
        for i in range(k):
            a1=heapq.heappop(h)
            res.append([a1[1],a1[2]])
        return res
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        mhap=[-x for x in count.values()]
        heapq.heapify(mhap)
        time=0
        q=deque()
        while mhap or q:
            time+=1
            if mhap:
                cnt=1+heapq.heappop(mhap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(mhap,q.popleft()[0])
        return time
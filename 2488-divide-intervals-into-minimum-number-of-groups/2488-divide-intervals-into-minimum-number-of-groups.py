class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        a=[]
        b=[]
        for l,r in intervals:
            a.append(l)
            b.append(r)
        a.sort()
        b.sort()
        i,j=0,0
        res=0
        groups=0
        while i<len(intervals) and j< len(intervals):
            if a[i]<=b[j]:
                groups+=1
                i+=1
            else:
                groups-=1
                j+=1
            res=max(groups,res)
        return res
        
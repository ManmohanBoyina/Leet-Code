class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        a=[]
        for i in range(len(intervals)):
            if not a or intervals[i][0]>a[-1][1]:
                a.append(intervals[i])
            else:
                a[-1][1]=max(intervals[i][1],a[-1][1])
        return a

        
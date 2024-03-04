class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a = []
        intervals.sort()
        if len(intervals) == 1:
            return intervals
        for i in range(len(intervals) - 1):
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i + 1][0] = intervals[i][0]
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
            else:
                a.append(intervals[i])
        a.append(intervals[-1])  # Append the last interval
        return a
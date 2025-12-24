class Solution(object):
    def minimumBoxes(self, apple, capacity):
        total=sum(apple)
        capacity.sort()
        m=len(capacity)
        count=0
        for i in range(m-1,-1,-1):
            total-=capacity[i]
            count+=1
            if total<=0:
                return count
        return -1

        
class Solution(object):
    def shortestToChar(self, s, c):
        ans=[]
        n=len(s)
        shortest_distance=n-1
        for i in range(n):
            if s[i]==c:
                shortest_distance=0
            ans.append(shortest_distance)
            shortest_distance+=1
        shortest_distance=n-1
        for i in range(n-1,-1,-1):
            if s[i]==c:
                shortest_distance=0
            ans[i]=min(ans[i],shortest_distance)
            shortest_distance+=1
        return ans
        

            
import collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi=0
        def dfs(i,j):
            nonlocal length
            if i<0 or j<0 or i==len(grid) or j==len(grid[0]) or grid[i][j]==0:
                return 0
            grid[i][j]=0
            length+=1
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        n = len(grid)
        graph = collections.defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    length=0
                    dfs(i,j)
                    maxi=max(maxi,length)
        return maxi
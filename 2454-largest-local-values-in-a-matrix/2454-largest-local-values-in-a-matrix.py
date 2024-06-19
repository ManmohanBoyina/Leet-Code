import numpy as np
class Solution(object):
    def largestLocal(self, grid):
        N = len(grid)-2
        res = [[0] * N for _ in range(N)]
        for i,j in product(range(N), range(N)):
            res[i][j] = max(grid[r][c] for r, c in product(range(i, i+3), range(j, j+3)))
        return res

            

        


        
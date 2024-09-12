class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        a=[]
        if m*n!=len(original):
            return []
        c=0
        for i in range(m):
            a.append(original[i * n:(i * n + n)])
        return a
        
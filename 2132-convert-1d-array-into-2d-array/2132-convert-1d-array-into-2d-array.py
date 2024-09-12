class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        a=[]
        if m*n!=len(original):
            return []
        c=0
        for i in range(m):
            b=[]
            for j in range(n):
                b.append(original[c])
                c+=1
            a.append(b)
        return a
        
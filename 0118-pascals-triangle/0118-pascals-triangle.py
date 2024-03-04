class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        a=[]
        if n>=1:
            col=[]
            col.append(1)
            a.append(col)
        if n>=2:
            col=[]
            col.append(1)
            col.append(1)
            a.append(col)
        i=3
        c=3
        while(i<=n):
            col=[]
            col.append(1)
            d=len(a[i-2])
            for j in range(d-1):
                col.append(a[i-2][j]+a[i-2][j+1])
            col.append(1)
            a.append(col)
            i=i+1
        return a
        
class Solution(object):
    def generate(self, numRows):
        a=[]
        if numRows>=1:
            col=[]
            col.append(1)
            a.append(col)
        if numRows>=2:
            col=[]
            col.append(1)
            col.append(1)
            a.append(col)
        i=3
        while(i<=numRows):
            col=[]
            col.append(1)
            for j in range(len(a[i-2])-1):
                col.append(a[i-2][j]+a[i-2][j+1])
            col.append(1)
            a.append(col)
            i=i+1
        return a
        


        
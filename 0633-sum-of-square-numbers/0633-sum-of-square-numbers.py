class Solution(object):
    def judgeSquareSum(self, c):
        i,j=0,int(math.sqrt(c))
        while i<=j:
            s=i*i+j*j
            if s==c:
                return True
            if s>c:
                j-=1
            else:
                i+=1
        return False

        
class Solution(object):
    def judgeSquareSum(self, c):
        if c==0:
            return True
        number=int(math.floor(math.sqrt(c)))
        for i in range(1,number+1):
            diff=c-i**2
            sdiff=math.sqrt(diff)
            if isinstance(sdiff, float) and sdiff == int(sdiff):
                sdiff = int(sdiff)
            if type(sdiff)==int and i**2+sdiff**2==c:
                return True
        return False

        
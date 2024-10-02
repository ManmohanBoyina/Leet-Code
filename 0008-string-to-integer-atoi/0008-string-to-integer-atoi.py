class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if s=="":
            return 0
        sign=1
        res,i=0,0
        if s[i]=="-":
            sign=-1
            i+=1
        elif s[i]=="+":
            i+=1
        def helper(res,i):
            if i>=len(s) or (s[i]>'9' or s[i]<'0'):
                return res
            res = res*10 + int(s[i])
            return helper(res,i+1)
        res=helper(res,i)
        if res*sign > 2**31 - 1:
            return 2**31-1
        elif res*sign < -(2**31):
            return -(2**31)
        else:
            return res*sign     
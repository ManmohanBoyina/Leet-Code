class Solution(object):
    def addBinary(self, a, b):
        carry=0
        res=''
        a=list(a)
        b=list(b)
        while a or b or carry:
            if a:
                carry+=int(a.pop())
            if b:
                carry+=int(b.pop())
            res+=str(carry%2)
            carry//=2
        return res[::-1]     
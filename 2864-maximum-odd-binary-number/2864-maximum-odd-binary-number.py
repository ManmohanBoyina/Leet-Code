class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        st=''.join(sorted(s))
        st=st[::-1]
        for i in range(len(st)):
            if st[i]=='0':
                c=list(st)
                c[i-1],c[len(s)-1]=c[len(s)-1],c[i-1]
                st=''.join(c)
                break
        return st
        
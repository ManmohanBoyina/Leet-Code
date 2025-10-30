class Solution(object):
    def countBinarySubstrings(self, s):
        a=[]
        c0,c1=0,0
        ans=0
        for i in range(len(s)):
            if s[i]=='0':
                if c1>0:
                    a.append(c1)
                    c1=0
                c0+=1
            else:
                if c0>0:
                    a.append(c0)
                    c0=0
                c1+=1
        if c1>0:
            a.append(c1)
        if c0>0:
            a.append(c0)
        print(a)
        for i in range(len(a)-1):
            ans+=min(a[i],a[i+1])
        return ans



        
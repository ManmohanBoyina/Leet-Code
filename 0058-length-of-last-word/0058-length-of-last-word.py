class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        res=[]
        res=s.split(' ')
        return len(res[-1])
        
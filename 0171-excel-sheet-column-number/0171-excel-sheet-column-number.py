class Solution(object):
    def titleToNumber(self, columnTitle):
        res=0
        for i in columnTitle:
            res=res*26+ord(i)-ord('A')+1
        return res
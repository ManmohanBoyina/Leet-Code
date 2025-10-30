class Solution(object):
    def validPalindrome(self, s):
        def isvalid(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True
        count=0
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return isvalid(left,right-1) or isvalid(left+1,right)
            else:
                left+=1
                right-=1
        return True
        
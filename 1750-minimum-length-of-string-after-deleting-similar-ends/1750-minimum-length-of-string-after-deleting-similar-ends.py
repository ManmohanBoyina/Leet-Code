class Solution(object):
    def minimumLength(self,s):
        left = 0
        right = len(s) - 1
        operations = 0
        while left < right and s[left]==s[right]:
            pos=s[left]
            while (left<len(s) and s[left]==pos):
                left+=1
            while(right>=0 and s[right]==pos):
                right-=1
        if right < left :
            return 0
        else:
            return right-left+1
            
        
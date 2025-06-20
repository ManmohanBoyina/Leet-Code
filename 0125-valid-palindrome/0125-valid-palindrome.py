class Solution(object):
    def isPalindrome(self, s):
        res=''
        s=s.lower()
        for i in s:
            if i.isalpha() or i.isdigit():
                res+=i
        return res==res[::-1]
        
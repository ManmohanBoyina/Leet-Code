class Solution(object):
    def isValid(self, s):
        dictt={"{":"}","[":"]","(":")"}
        stack=[]
        for i in s:
            if i=="{" or i=="(" or i=="[":
                stack.append(i)
            else:
                if len(stack)==0 or dictt[stack.pop()] != i:
                    return False
        return len(stack)==0
        
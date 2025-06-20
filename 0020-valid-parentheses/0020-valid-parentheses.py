class Solution(object):
    def isValid(self, s):
        stack=[]
        if len(s)==1:
            return False
        for i in s:
            if i=='(' or i=="[" or i=="{":
                stack.append(i)
            if i==")":
                if len(stack)!=0 and stack[-1]=="(":
                    stack.pop()
                else:
                    return False
            if i=="}":
                if len(stack)!=0 and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            if i=="]":
                if len(stack)!=0 and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
        return True if len(stack)==0 else False
        
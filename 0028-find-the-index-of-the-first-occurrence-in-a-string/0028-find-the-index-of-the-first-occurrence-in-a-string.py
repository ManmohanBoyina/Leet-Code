class Solution(object):
    def strStr(self, haystack, needle):
        word=len(needle)
        for i in range(len(haystack)-word+1):
            if needle==haystack[i:i+word]:
                return i
        return -1
        
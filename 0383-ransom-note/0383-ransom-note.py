class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d1=collections.Counter(ransomNote)
        d2=collections.Counter(magazine)
        for i in ransomNote:
            if i in d1 and i in d2:
                if d2[i]<d1[i]:
                    return False
            else:
                return False
        return True

        
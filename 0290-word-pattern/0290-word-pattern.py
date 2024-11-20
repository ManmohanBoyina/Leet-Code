class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = s.split()
        if len(pattern) != len(a):
            return False
        res = {}
        for i in range(len(pattern)):
            if pattern[i] not in res:
                if a[i] not in res.values():
                    res[pattern[i]] = a[i]
                else:
                    return False
            else:
                if res[pattern[i]] != a[i]:
                    return False
        return True

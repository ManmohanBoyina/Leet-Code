from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        b = Counter(s1)
        window = Counter()
        c = 0
        for i in range(len(s2)):
            window[s2[i]] += 1
            c += 1
            if c > len(s1):
                left_char = s2[i - len(s1)]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                c -= 1
            if window == b:
                return True
        
        return False



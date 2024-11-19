from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a=Counter(text)
        count=0
        while a['b']!=0 and a['a']!=0 and a['l']!=0 and a['o']!=0 and a['n']!=0:
            if a['b']>=1:
                a['b']-=1
            else:
                break
            if a['a']>=1:
                a['a']-=1
            else:
                break
            if a['l']>=2:
                a['l']-=2
            else:
                break
            if a['o']>=2:
                a['o']-=2
            else:
                break
            if a['n']>=1:
                a['n']-=1
            else:
                break
            count+=1
        return count
            
        
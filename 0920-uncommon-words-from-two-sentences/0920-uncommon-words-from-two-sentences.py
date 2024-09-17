class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=defaultdict(int)
        for word in s1.split()+s2.split():
            a[word]+=1
        return [w for w in a if a[w]==1]
        
        
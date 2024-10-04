class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        a=[]
        sum=0
        if len(skills)==2:
            return skills[0]*skills[1]
        skills.sort()
        i,j=0,len(skills)-1
        while i<j:
            if skills[i]+skills[j]==skills[i+1]+skills[j-1]:
                a.append((skills[i],skills[j]))
                sum+=(skills[i]*skills[j])
                i+=1
                j-=1
            else:
                return -1
        return sum

        
class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        a=[]
        if len(skills)==2:
            return skills[0]*skills[1]
        skills.sort()
        i,j=0,len(skills)-1
        while i<j:
            if skills[i]+skills[j]==skills[i+1]+skills[j-1]:
                a.append((skills[i],skills[j]))
                i+=1
                j-=1
            else:
                return -1
        sum=0
        for i in range(len(a)):
            sum+=(a[i][0]*a[i][1])
        return sum


        
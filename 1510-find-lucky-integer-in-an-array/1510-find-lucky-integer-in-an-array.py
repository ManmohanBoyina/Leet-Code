class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a={}
        for i in arr:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        maxi=-1
        for i in a.keys():
            if a[i]==i:
                maxi=max(maxi,i)
        return maxi
        
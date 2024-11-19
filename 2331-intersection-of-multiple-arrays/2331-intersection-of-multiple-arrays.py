class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        a={}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] not in a:
                    a[nums[i][j]]=1
                else:
                    a[nums[i][j]]+=1
        n=len(nums)
        ans=[]
        for i in a:
            if a[i]==n:
                ans.append(i)
        return sorted(ans)
        
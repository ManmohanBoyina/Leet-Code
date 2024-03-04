class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=[]
        nums.sort()
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                t=nums[i]+nums[j]+nums[k]
                if t>0:
                    k-=1
                elif t<0:
                    j+=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    j+=1
                    k-=1
                    a.append(temp)
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return a
        
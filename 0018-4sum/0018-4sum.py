class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a=[]
        nums.sort()
        sum1=0
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=len(nums)-1
                while k<l:
                    sum1=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum1>target:
                        l-=1
                    elif sum1<target:
                        k+=1
                    else:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        a.append(temp)
                        k+=1
                        l-=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
        return a
                


        
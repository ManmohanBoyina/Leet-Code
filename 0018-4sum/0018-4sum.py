class Solution(object):
    def fourSum(self, nums, target):
        a=[]
        nums.sort()
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=len(nums)-1
                while k<l:
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum<target:
                        k=k+1
                    elif sum>target:
                        l=l-1
                    else:
                        a.append([nums[i],nums[j],nums[k],nums[l]])
                        k=k+1
                        l=l-1
                        while k<l and nums[k]==nums[k-1]:
                            k=k+1
                        while k<l and nums[l]==nums[l+1]:
                            l=l-1
        return a
        
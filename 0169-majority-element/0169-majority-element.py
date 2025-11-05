class Solution(object):
    def majorityElement(self, nums):
        count={}
        res,maxCount=0,0
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
            else:
                count[nums[i]]+=1
            if count[nums[i]]>maxCount:
                maxCount=count[nums[i]]
                res=nums[i]
        return res

        
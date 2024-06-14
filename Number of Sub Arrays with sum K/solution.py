class Solution(object):
    def subarraySum(self, nums, k):
        s,count=0,0
        mp=defaultdict(int)
        mp[0]=1
        for i in range(len(nums)):
            s=s+nums[i]
            t=s-k
            count=count+mp[t]
            mp[s]=mp[s]+1
        return count

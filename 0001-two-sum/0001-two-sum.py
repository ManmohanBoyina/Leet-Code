class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tt={}
        for i in range(len(nums)):
            t=target-nums[i]
            if t in tt:
                return i, tt[t]
            tt[nums[i]]=i
        print(tt)
        return -1,-1
            
        
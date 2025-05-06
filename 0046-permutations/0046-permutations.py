class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        used=[False]*len(nums)
        def result(start_index):
            if start_index==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]==True:
                    continue
                path.append(nums[i])
                used[i]=True
                result(start_index+1)
                path.pop()
                used[i]=False
        result(0)
        return res

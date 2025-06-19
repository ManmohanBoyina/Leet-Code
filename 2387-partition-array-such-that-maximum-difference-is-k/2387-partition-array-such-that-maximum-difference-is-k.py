class Solution(object):
    def partitionArray(self, nums, k):
        res = []
        nums.sort()
        i = 0
        while i < len(nums):
            ans = []
            j = i + 1
            ans.append(nums[i])
            while j != len(nums):
                if nums[j] - nums[i] <= k:
                    ans.append(nums[j])
                    j += 1
                else:
                    break
            res.append(ans[:])
            i = j
        print(res)
        return len(res)
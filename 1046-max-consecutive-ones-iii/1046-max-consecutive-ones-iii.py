class Solution(object):
    def longestOnes(self, nums, k):
        i=0
        c,c1=0,k
        mlen=0
        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            while k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            mlen = max(mlen, j - i + 1)

        return mlen

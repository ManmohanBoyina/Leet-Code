class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        nums.reverse()
        i=0
        j=k-1
        while i<=j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        i,j=k,len(nums)-1
        while i<=j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        return nums

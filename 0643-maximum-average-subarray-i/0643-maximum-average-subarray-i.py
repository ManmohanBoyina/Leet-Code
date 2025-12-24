class Solution(object):
    def findMaxAverage(self, nums, k):
        i,j=0,k
        summ=float(sum(nums[i:j]))
        maxi=summ/k
        while j<len(nums):
            summ-=nums[i]
            i+=1
            summ+=nums[j]
            j+=1
            print(summ)
            avg=summ/k
            maxi=max(maxi,avg)
        return maxi
        
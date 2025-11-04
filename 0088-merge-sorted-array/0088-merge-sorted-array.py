class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j=n-1,0
        while i<m and j<n:
            if nums1[i]>nums2[j]:
                nums1[i],nums2[j]=nums2[j],nums1[i]
                i-=1
                j+=1
            else:
                break
        j=0
        for i in range(m,len(nums1)):
            nums1[i]=nums2[j]
            j+=1
        nums1.sort()
        return nums1
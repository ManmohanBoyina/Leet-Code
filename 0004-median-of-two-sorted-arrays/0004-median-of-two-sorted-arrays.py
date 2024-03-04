class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=sorted(nums1+nums2)
        t=len(a)
        if t%2==0:
          return (a[t//2]+a[(t//2)-1])/2
        return a[t//2]
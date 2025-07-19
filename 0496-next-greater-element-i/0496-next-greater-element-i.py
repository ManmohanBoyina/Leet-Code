class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[0]*len(nums1)
        hash_table = {num: i for i, num in enumerate(nums2)}
        j=0
        for num in nums1:
            i=hash_table[num]+1
            while i<len(nums2):
                if num<nums2[i]:
                    ans[j]=nums2[i]
                    break
                i+=1
            else:
                ans[j]=-1
            j+=1
        return ans        
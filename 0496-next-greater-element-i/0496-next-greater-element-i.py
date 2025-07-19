class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        stack=[]
        hash_map={}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if not stack:
                stack.append(nums2[i])
                hash_map[nums2[i]]=-1
            else:
                hash_map[nums2[i]]=stack[-1]
                stack.append(nums2[i])
        for num in nums1:
            ans.append(hash_map[num])
        return ans
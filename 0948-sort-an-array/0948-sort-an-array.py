class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        sorted_array = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        return sorted_array

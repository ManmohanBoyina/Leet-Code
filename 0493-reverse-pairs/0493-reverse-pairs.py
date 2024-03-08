class Solution(object):
    def reversePairs(self, nums):
        def count_and_merge(arr, low, mid, high):
            c = 0
            right = mid + 1
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1
                c += right - (mid + 1)
            temp = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1
            for i in range(low, high + 1):
                arr[i] = temp[i - low]
            return c
        def merge_sort_and_count(arr, low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            inversions = merge_sort_and_count(arr, low, mid) + merge_sort_and_count(arr, mid + 1, high)
            inversions += count_and_merge(arr, low, mid, high)
            return inversions
        n = len(nums)
        return merge_sort_and_count(nums, 0, n - 1)
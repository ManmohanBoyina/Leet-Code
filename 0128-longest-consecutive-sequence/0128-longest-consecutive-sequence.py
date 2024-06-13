class Solution(object):
    def longestConsecutive(self, nums):
        st=set()
        longest=1
        if len(nums)==0:
            return 0
        for i in nums:
            st.add(i)
        for i in st:
            if i-1 not in st:
                count=1
                t=i
                while t+1 in st:
                    t=t+1
                    count=count+1
                longest=max(longest,count)
        return longest

        
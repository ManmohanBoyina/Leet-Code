class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=[]
        res=[]
        c1,c2=0,0
        e1=float('-inf')
        e2=float('-inf')
        for i in range(len(nums)):
            if c1==0 and e2!=nums[i]:
                c1=1
                e1=nums[i]
            elif c2==0 and e1!=nums[i]:
                c2=1
                e2=nums[i]
            elif e1==nums[i]:
                c1=c1+1
            elif e2==nums[i]:
                c2=c2+1
            else:
                c1=c1-1
                c2=c2-1
        c1,c2=0,0
        for i in range(len(nums)):
            if nums[i]==e1:
                c1+=1
            if nums[i]==e2:
                c2+=1
        mini = int(len(nums)/ 3) + 1
        if c1 >= mini:
            res.append(e1)
        if c2 >= mini:
            res.append(e2)
        return res

        
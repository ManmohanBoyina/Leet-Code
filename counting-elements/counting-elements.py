class Solution:
    def countElements(self, arr: List[int]) -> int:
        a={}
        c=0
        for ind,val in enumerate(arr):
            a[val]=ind
        for i in arr:
            if i+1 in a:
                c+=1
        return c
                
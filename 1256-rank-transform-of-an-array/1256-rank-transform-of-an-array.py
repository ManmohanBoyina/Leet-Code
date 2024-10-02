from numpy import *
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        at=arr.copy()
        at.sort()
        a=defaultdict(int)
        c=1
        for i in range(len(arr)):
            if at[i] not in a:
                a[at[i]]=c
                c+=1
        for i in range(len(arr)):
            print(arr[i])
            arr[i]=a[arr[i]]
            
        return arr

        
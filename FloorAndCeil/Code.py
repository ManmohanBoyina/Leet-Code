def getFloorAndCeil(a, n, x):
    low=0
    high=n-1
    floor=-1
    ceil=-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]<=x:
            ceil=a[mid]
            low=mid+1
        else:
            high=mid-1
        if a[mid]>=x:
            floor=a[mid]
            high=mid-1
        else:
            low=mid+1
    return ceil,floor

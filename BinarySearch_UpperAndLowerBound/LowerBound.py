def lowerBound(arr: [int], n: int, x: int) -> int:
    low=0
    high=n-1
    ind=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ind=mid
            high=mid-1
        else:
            low=mid+1
    return ind

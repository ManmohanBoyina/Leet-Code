def upperBound(arr: [int], x: int, n: int) -> int:
    low=0
    high=n-1
    ind=0
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=x:
            ind=mid+1
            low=mid+1
        else:
            high=mid-1
    return ind

def binary_search(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
    return
arr=[2,4,5,17,52]
x=5
result=binary_search(arr,x)
if result !=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr = [55, 72, 62, 12, 41, 89, 22]
bubble_sort(arr)
print("Sorted Array: ", arr)
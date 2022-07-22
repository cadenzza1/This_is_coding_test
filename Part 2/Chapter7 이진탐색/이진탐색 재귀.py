def binary_search(array,start,end,key):
    if start>end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == key:
        return mid
    elif array[mid] > key:
        return binary_search(array,start,mid-1,key)
    elif array[mid] < key:
        return binary_search(array,mid+1,end,key)


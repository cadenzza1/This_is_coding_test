import sys
input = sys.stdin.readline

def binary_search(array,key,start,end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == key:
        return mid
    elif array[mid] > key:
        return binary_search(array,key,start,mid-1)
    elif array[mid] < key:
        return binary_search(array,key,mid+1,end)

n = int(input())
arr_n = list(map(int,input().split()))
arr_n.sort()

m = int(input())
arr_m = list(map(int,input().split()))

res_dict = {}
for i in arr_n:
    if not res_dict[i]:
        res_dict[i] = 1
    else:
        res_dict[i] += 1

res_arr = [0] * m

for x in arr_m:
    res = binary_search(arr_n,x,0,len(arr_n)-1)
    if res: # res값이 None이 아니면
        res_arr[arr_m.index(x)] += res_dict[x]
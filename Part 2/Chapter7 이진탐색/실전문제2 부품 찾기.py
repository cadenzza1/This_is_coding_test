import sys
input = sys.stdin.readline

def bin_search(array,key,start,end):
    if start > end:
        return None
    mid = (start + end ) // 2

    if array[mid] == key:
        return mid
    elif array[mid] > key:
        bin_search(array,key,start,mid-1)
    elif array[mid] < key:
        bin_search(array,key,mid+1,end)

n = int(input())
arr_n = list(map(int,input().split()))
arr_n.sort()
m = int(input())
arr_m = list(map(int,input().split()))

for i in arr_m:
    if bin_search(arr_n,i,0,n-1) == None:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')
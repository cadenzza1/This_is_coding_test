#ch6_b1 2470
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

tmp = sys.maxsize - 1


for i in range(n):
    for j in range(i+1,n): 
        if abs(arr[i] + arr[j]) < abs(tmp):
            tmp = arr[i] + arr[j]
            res_arr = [arr[i],arr[j]]

res_arr.sort()
for i in res_arr:
    print(i, end = ' ')
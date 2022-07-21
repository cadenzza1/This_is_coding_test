import sys
input = sys.stdin.readline

arr = []

n = int(input())
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    print(i,end = ' ')
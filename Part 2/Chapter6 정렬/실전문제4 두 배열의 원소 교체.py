import sys
input = sys.stdin.readline

n,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in range(k):
    a_min = min(a)
    b_max = max(b)
    if a_min < b_max:
        a[a.index(a_min)] , b[b.index(b_max)] = b_max, a_min
    else:
        continue

print(sum(a))
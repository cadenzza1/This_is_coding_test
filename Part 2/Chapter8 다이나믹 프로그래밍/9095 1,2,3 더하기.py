import sys
input = sys.stdin.readline

t = int(input())

test_case = []
for i in range(t):
    test_case.append(int(input()))

d = [0] * 11

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4,10+1):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for j in test_case:
    print(d[j])
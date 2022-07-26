import sys
input = sys.stdin.readline

x = int(input())

cnt = 0

while x != 1:
    if x // 5 == 0:
        x = x // 5
        cnt += 1
        continue
    elif x // 3 == 0:
        x = x // 3
        cnt += 1
        continue
    elif x // 2 == 0:
        x = x // 2
        cnt += 1
        continue
    else:
        x -= 1
        cnt += 1
        continue

print(cnt)
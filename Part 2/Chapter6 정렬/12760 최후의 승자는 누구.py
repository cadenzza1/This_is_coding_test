import sys
input = sys.stdin.readline

n, m = map(int,input().split())
card_arr = [] # 카드 배열의 정보가 들어가있는 배열
point_arr = [0] * n # 점수 정보가 들어가있는 배열
res = []

for _ in range(n):
    card_arr.append(sorted(list(map(int,input().split()))))

for i in range(m):
    tmp_arr = []
    for j in range(n):
        tmp_arr.append(card_arr[j][i])
    max_val = max(tmp_arr)
    for j in range(n):
        if tmp_arr[j] == max_val:
            point_arr[j] += 1

maax_val = max(point_arr)
for i in range(n):
    if point_arr[i] == maax_val:
        res.append(i+1)

for i in res:
    print(i, end = ' ')



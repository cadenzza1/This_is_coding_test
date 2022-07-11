# 시간제한 1초

import time
start_time = time.time()

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

cnt = 0 # 같은 수가 몇 번째 더해졌는지 확인할 변수
res = 0 # 값들을 더해 넣을 변수
for i in range(m):
    if cnt == k:
        cnt = 0
        res += arr[-2]
        continue
    cnt += 1
    res += arr[-1]

print(res)
end_time = time.time()
print(end_time-start_time)

# 주어진 배열을 정렬한 뒤 cnt변수를 이용해 k번만큼 더해질 때까지 arr[-1]을 더하고
# k에 달하면 arr[-2]를 더하는 식으로 해봤는데 4.9초나 걸렸다.... 정렬때문일까?

import time
start_time = time.time()

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort() # 입력받은 수 정렬
first = arr[-1] # 가장 큰 수
second = arr[-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
cnt = int(m / (k+1)) * k
cnt += m % (k+1)

res = 0
res += (cnt) * first # 가장 큰 수 더하기
res += (m - cnt) * second # 두 번째로 큰 수 더하기
print(res)
end_time = time.time()
print(end_time-start_time)

# 이게 개선된 코드라고는 하는데 막상 시간 3.5초 나온다... 머임...?
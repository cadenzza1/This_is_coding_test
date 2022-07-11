import time
start_time = time.time()

n,k = map(int,input().split())
cnt = 0 # 1이 될 때까지 계산 횟수
# n이 k로 나눠지는 수인지 확인한다.
while n != 1:
    if n % k == 0:
        cnt += 1
        n /= k
    else:
        cnt += 1
        n -= 1
print(cnt)

end_time = time.time()
print(end_time-start_time)
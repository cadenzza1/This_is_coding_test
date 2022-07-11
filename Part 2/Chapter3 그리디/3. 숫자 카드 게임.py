import time
start_time = time.time()

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

# 각 행을 순회하며 가장 작은 수를 찾기
min_num_arr = []
for i in range(n):
    min_num_arr.append(min(arr[i]))

print(max(min_num_arr))

end_time = time.time()
print(end_time-start_time)
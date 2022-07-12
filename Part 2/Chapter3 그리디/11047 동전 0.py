n, k = map(int,input().split())
arr = [] # 입력받은 동전의 종류를 저장할 배열
for i in range(n):
    arr.append(int(input()))
cnt = 0 # 필요한 동전 개수를 저장할 변수
arr.sort(reverse=True)


for i in arr:
    if i > k:
        continue
    else:
        cnt += k // i
        k = k - (k // i) * i

print(cnt)
    

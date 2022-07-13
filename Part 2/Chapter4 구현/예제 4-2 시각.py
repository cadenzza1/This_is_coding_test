n = int(input()) # '시'을 입력받음

cnt = 0  # 3이 포함된 시각의 개수를 저장할 변수

# 3중 반복문으로 시간 내에 3이 포함되어 있는지 확인하기
for i in range(n+1): # 시
    for j in range(60): # 분
        for k in range(60): # 초
            if '3' in (str(i) + str(j) + str(k)):
                cnt += 1

print(cnt)


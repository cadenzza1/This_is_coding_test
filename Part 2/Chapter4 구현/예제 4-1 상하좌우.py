n = int(input())
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1] # 방향벡터 사용
dy = [-1, 1, 0, 0] # 방향벡터 사용

x,y = 1,1 # 최초 시작 위치
move_types = ["L", "R", "U", "D"] # 이동하는 방식들 : 좌,우,상,하
 
for plan in plans: # 입력받은 이동 계획을 하나씩 받아온다.
    for i in range(len(move_types)): # move_types를 하나씩 읽어오며 plan과 대조하여 일치하는 타입의 이동을 실행한다.
        if plan == move_types[i]: # 이동 계획과 이동 타입이 같으면
            nx = x + dx[i] # 임시 x좌표에 값을 저장한다.
            ny = y + dy[i] # 임시 y좌표에 값을 저장한다. 
    if nx<1 or ny < 1 or nx > n or ny > n: # 근데 저장한 값이 타일을 벗어나면
        continue # 값을 대입하지 않고 새로운 이동 계획 받아온다.

    x,y = nx, ny # 타일을 벗어나지 않았다면 값을 대입한다.

print(x,y) # 최종 위치 출력
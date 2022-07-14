c, r = map(int,input().split())

k = int(input()) # 관객의 대기번호

if k > c*r:
    print(0)
    exit()

direction = 0 # 이동할 방향. 북 : 0 , 동 : 1 , 남 : 2 , 서 : 3
dx = [0,1,0,-1] # 북 동 남 서 이동에 따른 x좌표 변화
dy = [1,0,-1,0] # 북 동 남 서 이동에 따른 y좌표 변화
x,y = 1,1 # 최초 1,1에서 시작

d = [[0] * c for _ in range(r)] # 방문한 곳을 표시할 배열

cnt = 1 # 이동 횟수를 저장할 변수. 이동 횟수가 k와 같아지면 종료

temp_col = 0 # d배열에 사용할 열 인덱스
temp_row = r - 1 # d배열에 사용할 행 인덱스

def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0

while True:
    if cnt == k:
        print(x,y)
    d[temp_col][temp_row] = cnt
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx <= c and ny <= r and d[temp_col+dx[direction]][temp_row+dy[direction]] == 0:
        temp_col += dx[direction]
        temp_row += dy[direction]
        cnt += 1
        x = nx
        y = ny
    elif nx > c:
        turn_right()
        continue
    elif ny > r:
        turn_right()
        continue
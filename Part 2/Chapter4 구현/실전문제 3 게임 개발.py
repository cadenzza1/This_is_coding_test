n,m = map(int,input().split()) # n은 행의 개수, m은 열의 개수

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x좌표, y좌표, 바라보는 방향 입력받기
x, y, direction = map(int,input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

# 북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 메소드 정의
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1 # 최종 방문한 타일 개수
turn_time = 0 # 하나의 타일 위에서 회전한 횟수. 4 가 되면 더이상 방문할 곳이 없다는 뜻

while True:
    # 일단 왼쪽으로 회전부터!
    turn_left()
    nx = x + dx[direction] # 임시 x좌표
    ny = y + dy[direction] # 임시 y좌표
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1 # 방문한 타일 개수 1개 증가
        turn_time = 0 # 회전 횟수 초기화
        continue # 다시 처음부터 반복 시작!
    else:
        turn_time += 1 # 회전한 방향으로 진행하지 못한다면 회전횟수 1만큼 증가시키기!
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        # 뒤로 갈 수 있다면 이동하기
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else: 
            break # 더이상 움직일 수 없으므로 프로그램 종료
        turn_time = 0

print(cnt)



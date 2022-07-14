init_pos = input() # 최초 위치를 입력받는다
row = int(init_pos[1])
column = int(ord(init_pos[0])) - int(ord('a')) + 1 # 열 정보를 문자로 처리하지 않고 아스키값으로 처리하는 것이 포인트
print(column)

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,2),(1,2),(-1,-2),(1,-2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한 지 확인
res = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        res += 1

print(res)
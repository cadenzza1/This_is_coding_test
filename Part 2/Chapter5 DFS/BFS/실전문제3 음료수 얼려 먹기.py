n,m = map(int,input().split()) # 행과 열의 개수 입력받기

# 그래프 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m: # 배열 범위를 벗어나면
        return False # 함수 걍 종료
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y) # 상
        dfs(x+1,y) # 하
        dfs(x,y-1) # 좌
        dfs(x,y+1) # 우
        return True
    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            cnt += 1
    
print(cnt)
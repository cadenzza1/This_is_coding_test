import sys
input = sys.stdin.readline

n,m = map(int,input().split())
height = list(map(int,input().split())) # 보유중인 떡들의 높이 입력받기
height.sort()

start = 0 # 시작점 설정
end = max(height) # 최대 떡의 길이보다 큰 값으로 절단해봤자 의미가 없으니 최대값은 떡의 최대 길이로!

while start <= end:
    total = 0 # 잘린 떡의 길이의 합
    mid = (start+end)//2 # 절단기의 높이

    for x in height: # 떡들 하나씩 불러와서 자르기
        if x > mid:
            total += x-mid
    
    if total < m:
        end -= 1
        
    else:
        res = mid
        start += 1

print(res)
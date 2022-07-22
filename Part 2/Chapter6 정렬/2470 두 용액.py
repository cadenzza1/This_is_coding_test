#ch6_b1 2470
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

tmp = sys.maxsize - 1 # 더한 값을 저장할 변수
left = 0 # 왼쪽 포인터
right = n-1 # 오른쪽 포인터
one = 0 # 더할 왼쪽 수
two = 0 # 더할 오른쪽 수

while left < right: # 왼쪽 포인터가 오른쪽 포인터보다 작은 동안
    temp = arr[left] + arr[right] # 왼쪽 포인터 값과 오른쪽 포인터 값을 더한다
    res = abs(temp) # 더한 값을 절대값으로 저장

    if tmp > res: # 새로운 값이 기존의 값보다 작으면
        tmp = res # tmp에 새로운 값을 저장
        one = arr[left]
        two = arr[right]
    
    # 두 용액의 합이 양수라면 오른쪽 포인터를 줄여 값을 작게한다.
    if temp > 0:
        right -= 1
    # 두 용액의 합이 음수라면 왼쪽 포인터를 증가시켜 값을 크게한다.
    else:
        left += 1

print(one,two)
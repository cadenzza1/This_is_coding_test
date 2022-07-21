import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    input_data = input().split() # split은 공백을 기준으로 쪼개어 리스트 형식으로 반환!
    arr.append((input_data[0],int(input_data[1])))

arr.sort(key = lambda x : x[1])
for x,y in arr:
    print(x, end = ' ')
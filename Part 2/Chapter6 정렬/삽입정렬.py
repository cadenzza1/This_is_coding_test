arr = [2,4,5,1,0,7,9,8]

for i in range(1,len(arr)): # 삽입될 배열의 인덱스
    for j in range(i,0,-1): # 비교해나갈 배열의 인덱스
        if arr[j] < arr[j-1]:
            arr[j] , arr[j-1] = arr[j-1] , arr[j]
        else:
            break

print(arr)
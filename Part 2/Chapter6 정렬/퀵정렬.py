array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array,start,end): # 배열정보와, 시작 인덱스와, 종료 인덱스를 넘겨받는다.
    if start >= end: # 원소가 1개인 경우 종료. (재귀함수이므로 종료조건을 설정한 것임!)
        return
    pivot = start # 기준이 되는 피벗값을 시작 인덱스의 원소로 설정한다.
    left = start + 1 # 큰 값을 찾아가기 시작할 왼쪽 변수 설정
    right = end # 작은 값을 찾아가기 시작할 오른쪽 변수 설정

    while left <= right:
        # 피벗보다 큰 값을 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 값을 찾을 때까지 반복
        while left <= end and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot] , array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)

print(array)
    

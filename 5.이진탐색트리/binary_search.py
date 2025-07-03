"""
리스트값은 오름차순 정렬 되어있다고 가정
최초로 등장하는 target값의 인덱스값 구하기
"""

"""1. 반복문을 통한 구현"""
n = int(input())
n_list = list(map(int, input().split()))
target = int(input())
answer = -1

left = 0
right = len(n_list)-1 # 인덱스값으로 쓸 것이므로 -1 해주자

while left <= right:
    mid_idx = (left+right)//2
    if n_list[mid_idx] < target:
        left = mid_idx+1 
    elif n_list[mid_idx] > target:
        right = mid_idx-1
    else:
        answer = mid_idx
        right = mid_idx-1
        
print(answer)


"""2. 재귀를 통한 구현"""
# 기저조건: 데이터를 반으로 쪼개다가, 쪼개지 못하는 순간(start > end가 되는 순간) 종료
def binarysearch(arr:list, target, start:int, end:int) -> int: # start, end: 인덱스값
    """
    arr: Data
    args: target(찾고자 하는 값), start(시작 인덱스), end(끝 인덱스)
    return: 찾고자 하는 값의 인덱스값
    """
    if start > end:
        return None
    # 반올림 or 반내림 (여기서는 내림으로)
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarysearch(arr, target, start, mid-1)
    else:
        return binarysearch(arr, target, mid+1, end)

data = [1,2,3,4,5,6,7,8,9,10]
target = binarysearch(data, target=3, start=0, end=len(data)-1)
print(target)
    

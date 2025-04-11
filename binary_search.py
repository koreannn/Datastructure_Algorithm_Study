"""
리스트값은 오름차순 정렬 되어있다고 가정
최초로 등장하는 target값의 인덱스값 구하기
"""
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
# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
# 이 수열에서 x가 등장하는 횟수를 계산하라. 없으면 -1을 반환
# -10^9 <= 각 원소값 <=10^9 --> O(logN) 시간 복잡도로 구현해야 함

def find_start(numbers, mid):
    if numbers[mid]==x:
        return find_start(numbers, mid-1)
    else:
        return mid

def find_end(numbers, mid):
    if numbers[mid]==x:
        return find_end(numbers, mid+1)
    else:
        return mid

def binary_search(numbers, start, end, mid):
    if start==mid or end ==mid:
        return -1
    # 중간 값이 x보다 크면 end 를 mid로 바꾼 후 이진 탐색
    if numbers[mid] > x:
        end = mid
        return binary_search(numbers, start, end, (start+end)//2)
    # 중간 값이 x보다 작으면 start를 mid로 바꾼 후 이진 탐색
    elif numbers[mid]<x:
        start = mid
        return binary_search(numbers, start, end, (start+end)//2)
    # x가 있는 위치를 찾으면 시작위치, 끝 위치를 찾음
    elif numbers[mid]==x:
        start = find_start(numbers, mid)
        end = find_end(numbers, mid)
        answer = end - start - 1
        return answer

if __name__=="__main__":
    #### input ####
    N, x = 7, 2
    numbers = [1, 1, 1, 1, 1, 1, 3]
    ###############

    start = 0
    end = len(numbers)-1
    mid = (start+end)//2
    print(binary_search(numbers, 0, end, mid))
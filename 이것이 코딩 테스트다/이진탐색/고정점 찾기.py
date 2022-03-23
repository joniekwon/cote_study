# 고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미
# 하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며 모든 원소가 오름차순으로 정렬되어 있을 때 고정점이 있다면 고정점을 출력하는 프로그램을 작성하세요
# 고정점이 없다면 -1 출력

def binary_search(numbers, start, end, mid):
    if numbers[mid] == mid:
        return mid
    elif numbers[mid] < mid:
        start += 1
        return binary_search(numbers, start, end, (start+end)//2)
    elif numbers[mid] < mid:
        end -= 1
        return binary_search(numbers, start, end, (start+end)//2)
    elif start>end:
        return -1

if __name__=='__main__':
    # input
    N = 5
    numbers = [-15, -6, -1, 3, 7]

    start = 0
    end = N-1
    mid = (start+end)//2
    print(binary_search(numbers,start, end, mid))
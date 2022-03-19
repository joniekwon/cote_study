def binary_search(arr, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid + 1, end)

if __name__ == '__main__':
    arr = [1,3,5,7,9,11,13,15,17,19]
    target = 7

    res = binary_search(arr, target, 0, len(arr)-1)
    if res == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(res+1)
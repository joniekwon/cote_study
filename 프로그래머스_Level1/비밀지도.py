
def solution(n, arr1, arr2):
    answer = []
    for n1, n2 in zip(arr1,arr2):
        map1 = '0'* (n-len(bin(n1)[2:])) + bin(n1)[2:]
        map2 = '0'* (n-len(bin(n2)[2:])) + bin(n2)[2:]
        temp = ''
        for m1, m2 in zip(map1,map2):
            if m1=='1' or m2=='1':
                temp+='#'
            else:
                temp+=' '
        answer.append(temp)
    return answer

if __name__ == "__main__":
    n=5
    arr1=[9, 20, 28, 18, 11]
    arr2=[30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))
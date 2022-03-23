# 일직선상의 마을에 여러 채의 집이 위치해 있습니다.
# 이 중에서 특정 위치의 집에 특별히 한 개의 안테나를 설치하기로 결정 했습니다.
# 효율성을 위해 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치하려고 합니다.
# 안테나는 집이 위치한 곳에만 설치할 수 있고 논리적으로 동일한 위치에 여러개의 집이 존재하는 것이 가능합니다.
# 집들의 위치 값이 주어졌을 때 안테나를 설치할 위치를 선택하는 프로그램을 작성해주세요.
# 1 <= N <= 200,000

def solution(N, houses):
    l = [0] * (max(houses)+1)
    for x in houses:
        l[x] = 1

    answer = 0
    dist = int(1e9)
    for x in houses:
        temp = l
        temp[x] = 2
        d = 0
        for i in range(len(l)):
            if temp[i]==1:
                d += abs(i-x)
            if d < dist:
                dist = d
                answer = x
    return answer

# 어차피 안테나는 하나이고 거리는 인덱스로 계산 가능하므로
### 단순히 정렬 후 median을 찾으면 되는 문제..ㅠ

def solution2(N, houses):
    houses.sort()
    answer = houses[(N-1)//2]
    return answer

if __name__=="__main__":
    ### 입력 ###
    N = 4
    houses = [5, 1, 7, 9]
    ###########
    print(solution(N, houses))
    print(solution2(N, houses))
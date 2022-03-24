# 집 N개가 수직선 위에 있을 때 각각의 집의 좌표는 x(1),x(2),...,x(N) 이고 집 여러개가 같은 좌표를 가지는 일은 없습니다.
# 한 집에는 공유기를 하나만 설치할 수 있고 가장 인접한 두 공유기 사이의 거리를 가능한 크게하여 설치하려고 합니다.
# C개의 공유기를 N개의 집에 적당히 설치해서 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하세요.
from itertools import combinations
def solution(N, C, houses):
    install_points = list(combinations([x for x in range(N)], C)) # 공유기 설치할 인덱스 조합
    answer = 0
    for i, points in enumerate(install_points):
        dist = 1e9
        for p1, p2 in zip(points[:-1], points[1:]):
            dist = min(dist, abs(houses[p1]-houses[p2]))
        answer = max(answer, dist)

    return answer

# !!!! 집 좌표가 최대 10억 --> 이진 탐색으로 풀어야 함 ㅠㅠ
def solution2(N, C, houses):
    answer = 0
    return answer

if __name__=='__main__':
    # input
    N, C = 5, 3; houses = [1,2,8,4,9]
    #########
    houses.sort()
    # print(solution(N, C, houses))



    print(solution2(N, C, houses))
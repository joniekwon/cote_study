# N*N인 맵에서 도시의 각 칸은 빈칸(0), 치킨집(1) , 집(2) 중 하나
# 좌표는 (r,c) 형태로 나타내며 (1,1)부터 시작
# 폐업시키지 않을 치킨집을 M개 골랐을 때, 도시의 치킨 거리 최솟값을 출력
# 치킨거리는 집과 가장 가까운 치킨집 사이의 거리

# 구현 계획
# 1. map 입력 받고 집(2)을 기준으로 치킨집과의 치킨거리 구하기
# 2. 구한 치킨거리와 치킨집 좌표를 큐에 넣기(최대힙으로 사용: 음수로 바꾸어 넣기)
# 3. 치킨집이 M개를 초과하면(큐가 M개 초과) 현재 치킨거리와 비교하고 더 큰 거리를 가진 치킨집 폐업하기
# 4. 맵 순회 끝나면 큐에서 모든 원소 꺼내어 총 치킨거리 구하고 출력

# import heapq

# input
# N, M = 5, 3
# maps = [[0, 0, 1, 0, 0],
#         [0, 0, 2, 0, 1],
#         [0, 1, 2, 0, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 2]]
N,M = 5, 2
maps = [[0, 2, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [2, 0, 0, 1, 1],
        [2, 2, 0, 1, 2]]
# houses = []
# stores = []
# # 집과 치킨집 좌표 저장
# for i in range(len(maps)):
#     for j in range(len(maps)):
#         if maps[i][j] == 1:
#             stores.append([i,j])
#         elif maps[i][j] == 2:
#             houses.append([i,j])
# q = []
# for i in houses:
#     x1, y1 = i; x1+=1;y1+=1
#     dist = int(1e9)
#     for j in stores:
#         x2, y2 = j; x2+=1; y2+=1
#         temp = abs(x1-x2)+abs(y1-y2)
#         dist = min(dist, temp)
#     if len(q)<M:
#         heapq.heappush(q, -dist)
#     else:
#         # dist 가 같은곳이 있을 경우 에러 ..ㅎㅎ..
#         temp = heapq.heappop(q)[0]
#         heapq.heappush(q, max(-dist, temp))
# print(-sum(q))

#!!! 간과한것 --> 폐업시킬 경우 그 치킨집이 가장 가까웠던 집의 치킨거리를 다시 구해야함 ㅠㅠ
# 따라서 폐업하지 않을 치킨집의 조합으로 치킨거리를 모두 비교해야함.

from itertools import combinations

stores = []
houses = []
# # 집과 치킨집 좌표 저장
for i in range(len(maps)):
    for j in range(len(maps)):
        if maps[i][j] == 1:
            houses.append([i,j])
        elif maps[i][j] == 2:
            stores.append([i,j])

c = list(combinations(stores, M))
results= []
for x in range(len(c)):
    result = 0
    for i in houses:
        x1, y1 = i; x1 += 1; y1 += 1
        dist = int(1e9)
        for j in c[x]:
            x2, y2 = j; x2 += 1; y2 += 1
            temp = abs(x1-x2)+abs(y1-y2)
            dist = min(dist, temp)
        result += dist
    results.append(result)
print(min(results))
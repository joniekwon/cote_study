# 1<=n<=100개의 도시가 있고 한 도시에서 출발하여 다른 도시에 도착하는 1<=m<=100000개의 버스가 있습니다.
# 각 버스는 한 번 사용할 때 필요한 비용이 있습니다. 모든 도시의 쌍 A,B에 대하여 도시A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하세요.
import sys

N,M = 5,14
info = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
maps= [[int(1e9)]*(N+1) for _ in range(N+1)]

for start in range(1,N+1):
    for end in range(1,N+1):
        if start==end:
            maps[start][end]=0
for x in info:
    start, end, cost = x
    maps[start][end] = min(maps[start][end], cost)
for temp in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            # 그냥 가는것 보다 다른 곳을 거쳐서 갈때의 비용이 더 적으면 거쳐서 가기
            maps[start][end] = min(maps[start][end], maps[start][temp]+maps[temp][end])

for start in range(1, N+1):
    for end in range(1, N+1):
        if maps[start][end]==int(1e9):
            print(0, end=' ')
        else:
            print(maps[start][end], end=' ')
    print()

# input
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4
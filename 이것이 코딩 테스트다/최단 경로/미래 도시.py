# 1~N번까지의 회사가 있으며 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
# 방문 판매원 A는 현재 1번 회사에 위치해 있으며 X번 회사에 방문해 물건을 판매하고자 한다.
# 연결된 2개의 회사는 양방향으로 이동할 수 있고 1만큼의 시간으로 이동할 수 있다.
# A가 K번 회사에 방문한 뒤에 X번 회사로 갈 때 이동하게 되는 최소시간을 구해보자.
import sys

N, M = 5, 7  # N 회사 개수, M 경로 개수
X, K = 4, 5
info = [map(int, sys.stdin.readline().split()) for _ in range(M)]
maps = [[int(1e9)]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            maps[i][j] = 0
for x in info:
    start, end = x
    maps[start][end] = 1
    maps[end][start]=1

for k in range(N):
    for start in range(N):
        for end in range(N):
            maps[start][end] = min(maps[start][end], maps[start][k]+maps[k][end])
print(maps)

# 1 - K - X로 이동해야함
distance = maps[1][K]+maps[K][X]
if distance >= int(1e9):
    print(-1)
else:
    print(distance)
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
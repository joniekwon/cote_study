# N개의 도시가 있고 X도시에서 Y도시가 통로로 연결되어 있어야 전보를 보낼 수 있다.(단방향)
# C도시에서 최대한 많은 도시로 메시지를 보내고자 한다.
# C도시에서 보낸 메시지를 받는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는데 걸리는 시간은 얼마인지 출력하는 프로그램을 작성하시오
import heapq
import sys

# 3 2 1
# 1 2 4
# 1 3 2
N, M, C = map(int, sys.stdin.readline().split()) # 도시의 개수N, 통로의 개수M, 메시지를 보내고자하는 도시
info = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
maps = [[int(1e9)]*(N+1) for _ in range(N+1)]
for x in info:
    maps[x[0]][x[1]] = x[2]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            maps[i][j] = 0
distance = [-1] * (N+1)
distance[C] = 0
q = [C]
while q:
    start = heapq.heappop(q)
    for end in range(N+1):
        if distance[end] == -1:
            distance[end] = distance[start] + maps[start][end]
            q.append(end)
answer = [0, 0]
for i in range(1,N+1):
    if distance[i]<int(1e9) and distance[i]!=0:
        answer[0]+=1
        answer[1] = max(answer[1],distance[i])
print(answer[0], answer[1])


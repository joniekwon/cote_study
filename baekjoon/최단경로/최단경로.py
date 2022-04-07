import sys
import heapq
input = sys.stdin.readline

# V = 노드의 개수 E 간선의 개수
V, E = map(int, input().split())
start = int(input())

nodes = [[] for _ in range(V+1)]

# 거리 정보 저장
for info in range(E):
    u, v, w = map(int, input().split())
    nodes[u].append([v,w])
distance = [int(1e9)] * (V+1)
distance[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in nodes[now]:
        cost = dist+i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost,i[0]))
for i in range(1, V+1):
    if distance[i] >= int(1e9):
        print("INF")
    else:
        print(distance[i])
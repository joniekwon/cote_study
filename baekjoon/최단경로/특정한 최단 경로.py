import sys
import heapq
input = sys.stdin.readline

# N = 노드의 개수 E 간선의 개수
N, E = map(int, input().split())
nodes = [[] for _ in range(N+1)]

# 거리 정보 저장
for info in range(E):
    a, b, c = map(int, input().split())
    nodes[a].append([b,c])  # 양방향
    nodes[b].append([a,c])

def dijkstra(start, end):
    distance = [int(1e9)] * (N+1)
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
    return distance[end]
v1, v2 = map(int, input().split())

# 먼저 가는 순서에 따라 최단거리가 달라질 수 있으므로
answer = min(dijkstra(1, v1)+dijkstra(v1,v2)+dijkstra(v2,N), dijkstra(1, v2)+dijkstra(v2,v1)+dijkstra(v1,N))
if answer>=int(1e9):
    print(-1)
else:
    print(answer)
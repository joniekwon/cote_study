import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

visit = [float('inf')] * 200001
visit[n] = 0
answer = []
q = deque([n])
while q:
    nx = q.popleft()
    if nx == k:
        print(visit[nx])
        break

    if nx * 2 <= 100000 and visit[nx * 2] > visit[nx] + 1:
        q.append(nx * 2)
        visit[nx * 2] = visit[nx] + 1

    if nx > 0 and visit[nx - 1] > visit[nx] + 1:
        q.append(nx - 1)
        visit[nx - 1] = visit[nx] + 1

    if nx + 1 <= k and visit[nx + 1] > visit[nx] + 1:
        q.append(nx + 1)
        visit[nx + 1] = visit[nx] + 1
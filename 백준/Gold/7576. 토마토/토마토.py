import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]

q = []
tomato,  empty = 0, 0
for y in range(n): # y
    for x in range(m):  # x
        if farm[y][x] == 1:
            q.append((0, x, y))
            tomato += 1
        elif farm[y][x] == -1:
            empty += 1

if tomato + empty == m * n:
    print(0)
else:
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    count = 0
    q = deque(q)
    while q:
        day, x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and farm[ny][nx] == 0:
                q.append((day+1, nx, ny))
                farm[ny][nx] = 1
                count += 1
    print(day) if count == n * m - (tomato + empty) else print(-1)
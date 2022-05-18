import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
now_x, now_y = 0, 0 # 아기상어 위치
baby_shark = 2  # 아기상어 크기
total_time = 0    # 걸린 시간
ate_fish = 0 # 아기상어가 먹은 물고기 수

# 아기상어의 현재 위치 찾기
for y in range(n):
    for x in range(n):
        if maps[y][x] == 9:
            now_x, now_y = x, y
            maps[y][x] = 0

# 최단거리 맵 구하기
def bfs():
    dist = [[-1] * n for _ in range(n)]
    dist[now_y][now_x] = 0
    q = deque([(now_x, now_y)])
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and dist[ny][nx] == -1 and maps[ny][nx] <= baby_shark:
                dist[ny][nx] = dist[y][x] + 1
                q.append((nx, ny))
    return dist

# 최단거리 맵이 주어지면 가장 가까운 먹을 수 있는 물고기 먹으러 가기
def go_to_eat(dist_map):
    global now_x, now_y
    min_dist = int(1e9)
    for y in range(n):
        for x in range(n):
            if dist_map[y][x] != -1 and 1 <= maps[y][x] < baby_shark: # 도달할 수 있고, 아기상어보다 작은 물고기를 먹을 수 있음
                if dist_map[y][x] < min_dist:    # 가장 가까운 물고기 먹으러 가기
                    min_dist = dist_map[y][x]
                    now_x, now_y = x, y
    if min_dist == int(1e9):
        return None
    else:
        return min_dist

while True:
    time = go_to_eat(bfs())
    if time == None:
        print(total_time)
        break
    else:
        total_time += time
        ate_fish += 1
        maps[now_y][now_x] = 0

        if ate_fish >= baby_shark:
            baby_shark += 1
            ate_fish = 0
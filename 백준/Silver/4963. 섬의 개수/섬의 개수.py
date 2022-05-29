import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    directions = [(1, 1), (-1, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (0, -1), (-1, 0)]
    count = 0
    def dfs(x, y):
        if x < 0 or y < 0 or x >= w or y >= h or maps[y][x] == 0:
            return False
        else:
            maps[y][x] = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)
            return True

    for y in range(h):
        for x in range(w):
            if dfs(x, y) == True:
                count += 1
    print(count)
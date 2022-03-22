import heapq
###########
N = 6 # 정사각형 N*N칸
K = 3 # 사과의 수
locations = [[3,4],[2,5],[5,3]]

L = 3 # 방향 전환 횟수
directions = [[3,'D'], [15,'L'], [17,'D']] # 숫자: 초, L왼쪽으로 90도, D오른쪽으로 90도
########
commands= {}
for x in directions:
    sec, d = x
    commands[sec] = d

time = 0
snake = 1
maps = [[0]*N for _ in range(N)]
for apples in locations:
    x, y = apples
    maps[x-1][y-1] = 2

steps = {(1, 0) : [[-1,0],[0,1]],  #현재 진행 방향:동쪽, [다음 방향 왼쪽일때, 오른쪽일때]
         (0, 1) : [[0,-1],[0,1]],  #현재 진행 방향:남쪽
         (-1, 0) : [[1,0],[-1,0]], #현재 진행 방향:서쪽
         (0, -1) : [[0,-1],[1,0]]} #현재 진행 방향:북쪽
s = (1,0)
dx, dy = 0,0
q = [(time, (dx,dy))]
maps[0][0]=1
while time!=max(commands.keys()):
    time += 1
    # 현재 방향으로 한칸 이동
    dx += s[0]
    dy += s[1]

    # 이동할 위치가 맵을 벗어나거나 꼬리면 게임 중단
    if dy >= N or dx >= N or dy < 0 or dx < 0 or maps[dy][dx] == 1:
        print(time)
        break

    # 사과를 못먹었으면 지나온 곳 꼬리 지워주기 (큐에 넣은 순서대로 위치 빼기)
    if maps[dy][dx] != 2:
        _, (x, y) = heapq.heappop(q)
        maps[y][x] = 0
    else:  # 먹었으면 길이 늘리기
        snake += 1

    maps[dy][dx] = 1 # 뱀 위치 표시
    heapq.heappush(q, (time, (dx, dy))) #큐에 현재 위치 저장

    if time in commands.keys():
        if commands[time] == 'L':
            s = steps[s][0]
        else:
            s = steps[s][1]
import sys
from collections import deque

N, K = 3, 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
S,X,Y = 2,3,2
print(maps)

# K가지의 바이러스의 위치 정보가 주어졌을 떄 S초가 지난 후에 X,Y에 존재하는 바이러스의 종류를 출력
# 매 초 동서남북 방향으로 퍼짐, 이미 다른 바이러스가 있는 경우 퍼지지 못함, 1번부터 순서대로 전염 시작
# --> 1초에 1번증식 2초에 2번증식이 아니라 번호가 낮을수록 우선순위가 높다는 뜻이었음.ㅠㅠ 따라서 초 정보도 큐에 넣어야 함
x, y = 0, 0
virus = [x for x in range(1,K+1)]
time =0
q = []
for i in range(N):
    for j in range(N):
        if maps[i][j] != 0:
            q.append((maps[i][j], 0, i,j))
q.sort()
q = deque(q)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    virus, s, x, y = q.popleft()
    if s==S:
        break
    for i in range(4):
        x = x + dx[i]
        y = y + dy[i]
        if x>=0 and y>=0 and x<N and y<N and maps[x][y]==0:
            maps[x][y] = virus
            q.append((virus, s+1, x, y))

print(maps[X-1][Y-1])
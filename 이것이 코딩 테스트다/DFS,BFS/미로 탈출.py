# N*M 크기의 직사각형 형태의 미로에서 괴물을 피하여 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라
# 현재 위치 (1,1) 출구는 (N,M)에 존재, 괴물이 있는 곳은 0 없는 곳은 1로 표시
from collections import deque

def solution(N,M, maps):
    visit = deque()
    visit.append([0,0]) # 현재 위치

    # 이동할 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while visit:
        x, y = visit.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 맵을 벗어날 수 없음
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            # 괴물이 있는곳은 가지 않음
            if maps[nx][ny]==0:
                continue
            # 처음 방문할 경우에만 최단거리 기록
            if maps[nx][ny]==1:
                maps[nx][ny] = maps[x][y]+1
                visit.append([nx,ny])
    return maps[N-1][M-1]

if __name__=='__main__':
    N, M = 5, 6
    maps = ['101010',
            '111111',
            '000001',
            '111111',
            '111111']
    maps = [list(map(int, x)) for x in maps]
    print(solution(N,M,maps))

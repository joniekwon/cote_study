# N*M 크기의 직사각형 형태의 미로에서 괴물을 피하여 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라
# 현재 위치 (1,1) 출구는 (N,M)에 존재, 괴물이 있는 곳은 0 없는 곳은 1로 표시
from collections import deque

def solution(N,M, maps):
    answer = 0
    visit = deque()
    visit.append([0,0])
    x, y = 0, 0
    while True:
        if (x+1,y+1) == (N, M):
            break
        x, y = visit.popleft()
        answer+=1
        if y+1<M and maps[x][y+1] !=0:
            maps[x][y+1] = answer
            visit.append([x,y+1])
        if x+1<N and maps[x+1][y] !=0:
            maps[x + 1][y] = answer
            visit.append([x+1,y])
    return answer

# 1. 4가지 방향이 아닌 오른쪽, 아래쪽만으로 이동 --> 4방향으로 수정 필요,
# 2. 처음 방문하는게 아닐때는 거리 기록하지 않도록 해야함.

if __name__=='__main__':
    N, M = 5, 6
    maps = ['101010',
            '111111',
            '000001',
            '111111',
            '111111']
    maps = [list(map(int, x)) for x in maps]
    print(solution(N,M,maps))

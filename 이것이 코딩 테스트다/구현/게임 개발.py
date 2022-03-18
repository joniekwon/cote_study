import sys
# N*M 크기의 직사각형의 맵, 각각의 칸은 육지 혹은 바다, 상하좌우로 이동가능
# 1. 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
# 2. 왼쪽 방향에 가보지 않은 칸이 존재한다면 왼쪽방향으로 회전한 다음 왼쪽으로 한칸 이동. 가보지 않은 칸이 없으면 회전만 수행
# 3. 네 방향 모두 가본 곳이거나 바다이면 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 뒤쪽이 바다라면 움직임을 멈춘다.
def solution(N,M):
    answer = 1
    # A, B, d 캐릭터의 좌표 (A,B) / 방향 d (0:북 1:동 2:남 3:서)
    direct = [0, 1, 2, 3]
    step = [[0,-1],[1,0],[0,1],[-1,0]]
    back = [[0,1],[-1,0],[0,-1],[1,0]]
    A, B, d = map(int, sys.stdin.readline().strip().split())
    # 육지:0  바다:1
    maps = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
    # 처음 위치 방문 체크
    maps[B][A] = 'V'
    while True:
        # 왼쪽으로 방향 회전
        d = direct[d-1]
        # 이동할 좌표
        dA,dB = A+step[d][0], B+step[d][1]
        # 이동할 좌표가 맵 밖을 벗어나지 않을 경우만 계산
        if dA>=0 and dB>=0 and dA<N and dB<M:
            if maps[dA][dB] == 1 or maps[dA][dB] =='V':
                # 이동할 좌표가 바다이거나 방문한 장소면 한칸 뒤로 이동
                A,B = A+back[d][0], B+back[d][1]
                # 뒤로 간 좌표가 바다이면 종료
                if maps[B][A]==1:
                    break
                else:
                # 육지면 방문 체크
                    maps[B][A]='V'
                    answer+=1
            else:
            # 육지이고 방문한 장소가 아니면 방문 체크
                A, B = dA, dB
                maps[B][A] = 'V'
                answer+=1
    return answer

if __name__=='__main__':
    N, M = map(int, sys.stdin.readline().strip().split())

    print(solution(N,M))
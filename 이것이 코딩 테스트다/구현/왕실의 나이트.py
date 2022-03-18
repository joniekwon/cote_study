import sys
# 8x8 평면에 나이트 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수 출력

def solution(p):
    answer = 0
    x = 'abcdefgh'
    y = '12345678'
    p1 = x.index(p[0])
    p2 = y.index(p[1])
    # 나이트 이동 조건
    # 1. 수평으로 두칸 이동한 뒤에 수직으로 한칸
    # 2. 수직으로 두칸 이동한 뒤에 수평으로 한칸
    steps = [[2,1], [2,-1],[-2,1],[-2,-1],
             [1,2],[1,-2], [-1,2],[-1,-2]]
    for step in steps:
        position = [p1+ step[0],p2+step[1]]
        if position[0]>=0 and position[1]>=0 and position[0]<8 and position[1]<8:
            answer+=1

    return answer

if __name__=='__main__':
    p = sys.stdin.readline().strip()
    print(solution(p))
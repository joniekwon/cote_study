import sys
# 정수 N이 입력되었을때 00시00분00초에서 N시 59분 59초까지의 모든 시각중에서 N이 포함되어있는 모든 경우의 수를 구하라.
def solution(N):
    count = 0

    for h in range(N+1):
        #h시
        for m in range(60):
            #m분
            for s in range(60):
                #s초
                if (str(N) in str(h)) or (str(N) in str(m)) or (str(N) in str(s)):
                    count+=1
    return count

if __name__=='__main__':
    N = int(sys.stdin.readline())
    print(solution(N))
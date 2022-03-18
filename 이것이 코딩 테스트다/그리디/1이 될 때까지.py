import sys

def solution(N, K):
    answer = 0
    while N!=1:
        if N%K==0:
            N //= K
        else:
            N -=1
        answer += 1

    return answer

if __name__=='__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    print(solution(N, K))
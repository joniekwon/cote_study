import sys

def solution(N,M):
    answer = [0]*N
    for i in range(N):
        nums = list(map(int, sys.stdin.readline().strip().split()))
        answer[i] = min(nums)
    return max(answer)

if __name__=='__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    print(solution(N,M))
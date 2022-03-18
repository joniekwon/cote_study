import sys
def solution(N, M, K):
    answer = [0]*M
    # 총 M개의 숫자 더함, K번까지 연속으로 더할 수 있음,
    # 결국 필요한 숫자는 가장 큰 숫자1, 두번째로 큰 숫자1 총 2개
    nums = sorted(list(map(int, sys.stdin.readline().strip().split())))
    n1 = nums[-1]
    n2 = nums[-2]

    # answer = [n1]*K + [n2]
    # 가장 큰 수가 더해지는 횟수
    count = M//(K+1) * K
    count += M%(K+1) # 나머지

    # 따라서 다음 수가 더해지는 횟수는 M - count
    answer = n1*count
    answer += n2*(M-count)

    return answer

if __name__=='__main__':
    N, M, K = map(int, sys.stdin.readline().strip().split())
    print(solution(N, M, K))
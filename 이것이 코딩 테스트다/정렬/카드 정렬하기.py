# N개의 숫자 카드묶음의 각각의 크기가 주어질 때, 최소한 몇번의 비교가 필요한지를 구하는 프로그램을 작성하세요
def solution(N,M):
    M.sort()
    answer = 0
    stack = []
    for x in M:
        stack.append(x)
        if len(stack)==2:
            s = sum(stack)
            stack.append(s)
            answer+=s
            stack = stack[-1:]
    return answer

### 정렬하지 않고 heapq로 구현하기
import heapq
def solution2(N,M):
    answer = 0
    q = []

    for x in M:
        heapq.heappush(q,x)

    while len(q)!=1:
        n1 = heapq.heappop(q)
        n2 = heapq.heappop(q)
        s = n1+n2
        answer+=s
        heapq.heappush(q,s)

    return answer


if __name__=="__main__":
    # input
    N = 3
    M = [40, 20, 10, 50]
    print(solution2(N,M))
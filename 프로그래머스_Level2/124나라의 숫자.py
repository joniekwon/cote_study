from collections import deque

def solution(n):
    answer = deque()
    while n>0:
        r = n % 3
        n = n // 3

        if r==0:
            n -= 1
            r = 4
        answer.appendleft(str(r))
    return ''.join(answer)
if __name__=='__main__':
    n = 4
    print(solution(n))

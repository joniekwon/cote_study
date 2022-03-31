import sys
input = sys.stdin.readline
n = int(input())
q = list(map(int, input().split()))
#대기시간이 적을수록 최종 시간이 줄어들기 때문에 적게 걸리는 시간부터 오름차순 정렬
q.sort()
answer = [0] * n
answer[0] = q[0]
#i번째 사람은 대시시간(i-1까지 걸리는시간) + 본인이 걸리는 시간 이므로
for i in range(1,len(q)):
    answer[i] = answer[i-1]+ q[i]
print(sum(answer))
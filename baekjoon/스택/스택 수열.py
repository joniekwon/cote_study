import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# 수열 입력 받기
nums = deque()
for _ in range(n):
    nums.append(int(input()))

q = []
answer = []
i = 1
isPossible = True

while i<=n:
    # 스택에서 빼낼 수 있는 숫자와 수열의 맨 앞의 숫자가 같으면 pop
    if q and q[-1] == nums[0]:
        q.pop()
        nums.popleft()
        answer.append("-")
        continue

    # 큐가 비어있거나 뺴낼 수 없으면 다음 숫자 push
    q.append(i)
    answer.append("+")
    i+=1

# 스택에서 하나씩 빼서 수열과 비교
for i in range(len(q)):
    if q.pop() == nums[i]:
        answer.append("-")
        continue
# 스택과 순열의 숫자가 다르면 불가능. 순회 종료
    else:
        print("NO")
        isPossible = False
        break

# 가능하다면 정답 출력
if isPossible:
    for c in answer:
        print(c)

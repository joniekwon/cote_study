# N개의 숫자 카드묶음의 각각의 크기가 주어질 때, 최소한 몇번의 비교가 필요한지를 구하는 프로그램을 작성하세요
# input
N = 3
M = [40, 20, 10, 50]
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

print(answer)
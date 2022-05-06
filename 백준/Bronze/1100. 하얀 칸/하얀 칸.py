import sys
input = sys.stdin.readline
answer = 0
for i in range(8):
    row = input().rstrip()
    if i % 2 == 0:
        answer += row[::2].count('F')
    else:
        answer += row[1::2].count('F')
print(answer)
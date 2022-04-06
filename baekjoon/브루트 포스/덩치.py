import sys
input = sys.stdin.readline

n = int(input())
people = []
# 키, 몸무게 입력받기
for i in range(n):
    weight, height = map(int, input().split())
    people.append((weight,height,i))
# 내림차순 정렬
people.sort(key=lambda x:(-x[0], -x[1]))
answer = [1] * n
for i in range(len(people)):
    w1, h1, index1 = people[i]
    for j in range(len(people)):
        w2, h2, index2 = people[j]
        # 덩치가 더 큰 사람이 존재할 경우 랭크 늘리기
        if w2 < w1 and h2 < h1:
            answer[index2] +=1
print(*answer)

# 6
# 8 9
# 10 8
# 40 3
# 4 5
# 2 54
# 39 4
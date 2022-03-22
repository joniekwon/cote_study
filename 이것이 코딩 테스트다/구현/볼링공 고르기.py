# 볼링공의 개수(N)와 무게(1~M)가 주어지고, 두 사람이 서로 다른 무게의 볼링공을 골라야 할 때 두사람이 고를 수 있는 볼링공 번호의 조합을 구해보자.
from itertools import combinations

# N, M = 5, 3
# weights = [1,3,2,3,2]

N, M = 8, 5
weights = [1, 5, 4, 3, 2, 4, 5, 2]

candidates = list(combinations([x for x in range(N)],2))
answer = 0
for w in candidates:
    p1, p2 = w
    if weights[p1]!=weights[p2]:
        answer+=1
print(answer)
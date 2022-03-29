# 11047번: 동전 0
# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
values = []
# 동전의 종류
for i in range(N):
    values.append(int(input()))
# answer
count = 0
# index (큰 단위의 동전부터 사용하기 위해)
i=len(values)-1

while K>0:  # K원을 만들면 종료
    # 최대 단위의 동전을 사용할 수 있는만큼 사용하고 사용된 값 만큼 빼주기
    v = K // values[i]
    if v > 0:
        K -= (values[i] * v)
        count+= v
    else:
    # 사용할 수 없는 단위면 다음 단위의 동전 사용
        i-=1
        continue
print(count)

# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000
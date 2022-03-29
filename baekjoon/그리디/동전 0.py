import sys
input = sys.stdin.readline
N, K = map(int, input().split())
values = []
for i in range(N):
    values.append(int(input()))
count = 0
i=len(values)-1
while K>0:
    v = K // values[i]
    if v > 0:
        K -= (values[i] * v)
        count+= v
    else:
        i-=1
        continue
print(count)

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
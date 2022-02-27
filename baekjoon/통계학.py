import sys
from collections import Counter
N = int(sys.stdin.readline())
nums = [0]*N
for i in range(N):
    nums[i] = int(sys.stdin.readline())
print("%d" %round(sum(nums)/N,0))
print(sorted(nums)[N//2])
c = Counter(nums)
most_ = list(map(list, zip(*sorted(c.most_common(), key=lambda x:x[1], reverse=True))))
max_cnt = most_[1].count(max(most_[1]))
if max_cnt==1:
    print(most_[0][0])
else:
    print(sorted(c.most_common(max_cnt))[1][0])
print(abs(max(nums)-min(nums)))
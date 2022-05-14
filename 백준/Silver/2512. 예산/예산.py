import sys

input = sys.stdin.readline
n = int(input())
budget = list(map(int, input().split()))
total = int(input())
if sum(budget) <= total:
    print(max(budget))
else:
    start, end = 0, total

    answer = 0
    while start <= end:
        mid = (start + end) // 2

        bdg_sum = 0
        for bdg in budget:
            bdg_sum += min(mid, bdg)

        if bdg_sum <= total:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)
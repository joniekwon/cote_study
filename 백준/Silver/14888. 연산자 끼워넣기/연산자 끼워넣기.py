import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

max_sum, min_sum = -int(1e9), int(1e9)
add, sub, mul, div = map(int, input().split())

def dfs(i, now):
    global min_sum, max_sum, add, sub, mul, div

    if i == n:
        min_sum = min(min_sum, now)
        max_sum = max(max_sum, now)
    else:

        if add > 0:
            add -= 1
            dfs(i + 1, now + nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * nums[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / nums[i]))
            div += 1

dfs(1, nums[0])
print(max_sum)
print(min_sum)
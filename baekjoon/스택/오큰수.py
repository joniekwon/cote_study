import sys
# N 이 100만까지, 재귀 depth max 1000까지여서 런타임 에러 (RecursionError)발생 ㅠ
# def find_o(n, nums,index):
#     if nums[index]>n:
#         return nums[index]
#     else:
#         return find_o(n, nums, index+1)
#
# input = sys.stdin.readline
# n = int(input())
# nums = list(map(int, input().split()))
# answer = [0] * n
#
# for i in range(n):
#     if i==n-1:
#         answer[i] = -1
#     else:
#         answer[i] = find_o(nums[i], nums, i+1)
#
# for i in answer:
#     print(i, end=' ')


# 스택으로 다시 풀기
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
answer = [-1] * n
stack = []
for i in range(n):
    while stack and nums[stack[-1]]<nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)
print(*answer)
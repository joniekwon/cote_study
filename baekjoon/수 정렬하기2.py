import sys
N = int(sys.stdin.readline())
nums = [0]*N
for i in range(len(nums)):
   nums[i] = int(sys.stdin.readline())
for i in sorted(nums):
   print(i)
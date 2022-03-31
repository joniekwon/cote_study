import sys
input = sys.stdin.readline
s = input().rstrip()
# 숫자만 분리
nums = s.replace("-", ' ')
nums = nums.replace("+", ' ')
nums = list(map(int, nums.split()))
# +, - 문자열만 분리
s = [x for x in s if not x.isdigit()]
# - 없으면 다 더하는 수 밖에 없으므로 그냥 전체 합 반환
if not "-" in s:
    print(sum(nums))
# 있을 경우 - 뒤의 숫자를 다 더해서 빼는게 가장 작은 수를 만들 수 있음
else:
    i = s.index("-")
    sum1 = sum(nums[:i+1])
    sum2 = sum(nums[i+1:])
    print(sum1-sum2)
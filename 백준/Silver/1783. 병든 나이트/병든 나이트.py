import sys
input = sys.stdin.readline
n, m = map(int, input().split())
if n == 1:  # 이동불가
    print(1)
elif n == 2: 
    print(min(4, (m + 1) // 2))
elif m < 7:  
    print(min(4, m))
else:
    print(m - 7 + 5)
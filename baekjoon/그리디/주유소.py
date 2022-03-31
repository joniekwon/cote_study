import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))
temp = int(1e9)
answer = 0
# 현재위치보다 이전 위치의 가격이 더 저렴하면 이전 가격으로 주유하고 가기
for i, price in enumerate(prices[:-1]):
    if temp>price:
        temp=price
    answer += roads[i] * temp
print(answer)
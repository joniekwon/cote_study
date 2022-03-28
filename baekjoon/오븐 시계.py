import sys

input = sys.stdin.readline
# 디지털 시계 0시 0분  ~ 23시 59분
# 시작하는 시,분이 주어졌을 때 끝나는 시각 출력
hour, minute = map(int, input().split())
time = hour*60 + minute
time += int(input())
hour = (time//60)%24
minute = time%60
print(hour, minute)
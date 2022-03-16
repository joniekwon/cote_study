import sys
N = int(sys.stdin.readline())
members = [0] * N
for i in range(N):
    age, name = sys.stdin.readline().split()
    members[i] = (name, int(age)) ##### int로 안바꾸고 문자열로 정렬해서 엄청틀림 ㅠㅠ

for i in sorted(members, key=lambda x: x[1]):
    name, age = i
    print(age, name)

import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    number_book = [input().rstrip() for _ in range(n)]
    number_book.sort()
    for x, y in zip(number_book[:-1], number_book[1:]):
        if x == y[:len(x)]:
            print("NO")
            break
    else:
        print("YES")
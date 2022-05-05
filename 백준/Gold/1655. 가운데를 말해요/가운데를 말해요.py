import sys
import heapq
input = sys.stdin.readline
n = int(input())
min_heap = []
max_heap = []
a = 0
for _ in range(n):
    x = int(input())
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)

    if min_heap and min_heap[0] < -max_heap[0]:
        a = heapq.heappop(min_heap)
        b = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, b)
        heapq.heappush(max_heap, -a)

    if min_heap:
        print(min(min_heap[0],-max_heap[0]))
    else:
        print(-max_heap[0])
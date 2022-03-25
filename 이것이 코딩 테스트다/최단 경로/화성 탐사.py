import sys
import heapq
def solution(n, info):
    # info = [list(map(int, sys.stdin.readline())) for _ in range(N)]
    costs = [[int(1e9)]*n for _ in range(n)]
    costs[0][0]=info[0][0]

    dx= [1,-1,0,0]
    dy = [0,0,1,-1]

    q = []
    heapq.heappush(q, [costs[0][0], 0,0])
    while q:
        dist, x, y = heapq.heappop(q)
        if costs[x][y] < dist:
            continue

        for i in range(4):
            x += dx[i]
            y += dy[i]
            if x<0 or y<0 or x>=n or y>=n:
                continue

            cost = dist + info[x][y]
            if cost < costs[x][y]:
                costs[x][y] = cost
                heapq.heappush(q, [cost, x,y])

    return costs[n-1][n-1]


if __name__ == '__main__':
    N = [3,5,7]
    info = [[[5,5,4] , [3,9,1], [3,2,7]] ,
            [[3,7,2,0,1],[2,8,0,9,1],[1,2,1,8,1],[9,8,9,2,0],[3,6,5,1,5]],
            [[9,0,5,1,1,5,3],[4,1,2,1,6,5,3],[0,7,6,1,6,8,5],[1,1,7,8,3,2,3],[9,4,0,7,6,4,1],[5,8,3,2,4,8,3],[7,4,8,4,8,3,4]]]
    for i,j in zip(N,info):
        print(solution(i,j))
import sys

def solution(N):
    maps = [1,1]
    commands = sys.stdin.readline().strip().split()
    for c in commands:
        if c=='R' and maps[1]+1<=N:
            maps[1]+=1
        elif c=='L' and maps[1]-1>=1:
            maps[1] -=1
        elif c=='U' and maps[0]-1>=1:
            maps[0] -=1
        elif c=='D' and maps[0]+1<=N:
            maps[0] +=1
    return print(maps[0], maps[1])

if __name__=='__main__':
    N = int(sys.stdin.readline())
    solution(N)
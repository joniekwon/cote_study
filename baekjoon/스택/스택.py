import sys
N = int(sys.stdin.readline())
q = []
for _ in range(N):
    command = sys.stdin.readline().strip()
    if command.split()[0]=='push':
        command, number = command.split()
        q.append(int(number))
    elif command=='pop':
        try:
            print(q.pop())
        except:
            print(-1)
    elif command=='size':
        print(len(q))
    elif command=='empty':
        print(0 if len(q) else 1)
    elif command=='top':
        try:
            print(q[-1])
        except:
            print(-1)

def dfs(networks, start):
    visit = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            # 1과 2가 이어져 있으면 2에서 갈 수 있는 경로도 연결되어 있으므로 2와 이어진 경로를 1의 경로로 포함
            stack.extend(networks[node])
    return visit


def solution(n, computers):
    networks = {x:[] for x in range(n)}
    for start in range(n):
        for end in range(n):
            if start!=end and computers[start][end]==1:
                networks[start].append(end)
    path = list(map(sorted,[dfs(networks, start) for start in networks]))
    path = [''.join(map(str,x)) for x in path]
    return len(set(path))

if __name__=='__main__':
    n=3
    computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))


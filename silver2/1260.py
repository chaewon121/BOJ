from collections import deque

n, m, a = map(int, input().split())
data = []
for i in range(m):
    data.append(list(map(int, input().split())))

result = [[] for _ in range(n + 1)]

for i in range(m):
    result[data[i][1]].append(data[i][0])
    result[data[i][0]].append(data[i][1])

for i in range(n + 1):
    result[i].sort()


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited1):
    qu = deque([start])
    visited1[start] = True
    while qu:
        v = qu.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited1[i]:
                qu.append(i)
                visited1[i] = True


visited = [False] * (n + 1)
visited1 = [False] * (n + 1)

dfs(result, a, visited)
print()
bfs(result, a, visited1)
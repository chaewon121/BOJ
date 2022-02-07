from collections import deque

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
visit = [[1] * n for _ in range(n)]


def bfs(x, y):
    qu = deque()

    qu.append((x, y))

    while qu:

        x, y = qu.popleft()
        a = data[x][y]
        if (x == n - 1 and y == n - 1):
            break
        else:

            if 0 <= x + a <= n - 1 and 0 <= y <= n - 1 and visit[x + a][y] == 1:
                qu.append((x + a, y))
                visit[x + a][y] = 0
            if 0 <= x <= n - 1 and 0 <= y + a <= n - 1 and visit[x][y + a] == 1:
                qu.append((x, y + a))
                visit[x][y + a] = 0

            else:
                continue


bfs(0, 0)
if visit[n - 1][n - 1] == 0:
    print("HaruHaru")
else:
    print("Hing")

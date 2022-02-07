n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(input()))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if data[x][y] == "-":
        data[x][y] = "*"
        if 0 <= x < n and 0 <= y + 1 < m and data[x][y + 1] == "-":
            dfs(x, y + 1)

        return True
    if data[x][y] == "|":

        data[x][y] = "*"
        if 0 <= x + 1 < n and 0 <= y < m and data[x + 1][y] == "|":
            dfs(x + 1, y)
        return True
    return False


cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)
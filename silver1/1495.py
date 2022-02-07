import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**6)
# 개선된 다익스트라 알고리즘 소스코드
n, s, m = map(int, input().split())
data = list(map(int, input().split()))
result = result = [[0] * (m + 1) for _ in range(n)]
if 0 <= s - data[0] <= m:
    result[0][s - data[0]] = 1
if 0 <= s + data[0] <= m:
    result[0][s + data[0]] = 1

for i in range(0, n - 1):
    for j in range(m + 1):

        if result[i][j] == 1:

            if 0 <= j - data[i + 1] <= m:
                result[i + 1][j - data[i + 1]] = 1
            if 0 <= j + data[i + 1] <= m:
                result[i + 1][j + data[i + 1]] = 1
max = -1
for i in range(m, -1, -1):

    if result[n - 1][i] == 1:
        max = i
        break
print(max)
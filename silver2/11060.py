import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**6)
# 개선된 다익스트라 알고리즘 소스코드
n = int(input())
data = list(map(int, input().split()))
result = [n + 1] * n
result[0] = 0

for i in range(n):
    flag = 0
    for j in range(data[i]):
        if i + j + 1 > n - 1:
            break
        result[i + j + 1] = min(result[i + j + 1], result[i] + 1)

if result[n - 1] == n + 1:
    print(-1)
else:
    print(result[n - 1])
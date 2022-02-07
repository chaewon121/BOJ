import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

data = []

for i in range(n):
    data.append(int(input()))

result = [0] * (k + 1)
result[0] = 1

for i in data:
    for j in range(i, k + 1):
        result[j] = result[j] + result[j - i]

print(result[k])
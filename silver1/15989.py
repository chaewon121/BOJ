import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**6)
# 개선된 다익스트라 알고리즘 소스코드
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

for i in range(n):
    a = data[i]
    cnt = 0
    cnt += (a // 3) + 1
    while (a >= 0):
        a = a - 2
        cnt += (a // 3) + 1

    print(cnt)
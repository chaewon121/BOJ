import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))
data.sort()

start = 1  # 1

end = data[n - 1] - data[0]  # 5
# a는 거리의 최대값

while start <= end:
    mid = (end + start) // 2

    cnt = 1  # 첫번째 자리에 먼저 설치

    a = min(data) + mid
    for i in range(1, len(data)):
        if data[i] >= a:
            cnt += 1
            a = (data[i]) + mid

    if cnt >= (m):
        start = mid + 1
    else:
        end = mid - 1

print(end)
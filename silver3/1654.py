import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**6)
n, k = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))

start = 1
end = max(data)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in data:
        cnt += (i // mid)

    if cnt >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)
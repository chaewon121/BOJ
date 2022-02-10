import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)


while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in data:
        a = 0
        if i <= mid:
            a = 0
        else:
            a = i - mid
        cnt += a

    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
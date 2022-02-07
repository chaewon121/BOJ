import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**6)
n = int(input())
cnt = 0
result = 0
for i in range(666, 1000000000):
    a = []
    cnt1 = 0
    for j in str(i):
        a.append(j)
    for k in a:
        if k == "6":
            cnt1 += 1
            if cnt1 >= 3:
                cnt += 1
                break
        else:
            cnt1 = 0

    if cnt == n:
        result = i
        break
print(result)

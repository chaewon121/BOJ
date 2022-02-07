import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**6)

n = int(input())
array = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))
array.sort()

for i in card:
    result = 0
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == i:
            result = 1
            print(1, end=" ")
            break
        elif array[mid] > i:
            end = mid - 1
        else:
            start = mid + 1

    if result == 0:
        result = None
        print(0, end=" ")
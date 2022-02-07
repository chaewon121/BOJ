import sys
input = lambda : sys.stdin.readline().rstrip()
#sys.setrecursionlimit(10**6)

n,k=map(int,input().split())

data=[]

for i in range(n):
    data.append(int(input()))

result=[10001]*(k+1)
result[0]=0

for i in range(n):
    for j in range(data[i],k+1):
        result[j]=min(result[j],result[j-data[i]]+1)
if result[k]==10001:
    print(-1)
else:
    print(result[k])
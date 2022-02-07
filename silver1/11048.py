import sys

input = lambda : sys.stdin.readline().rstrip()
#sys.setrecursionlimit(10**6)
#개선된 다익스트라 알고리즘 소스코드
n,m=map(int,input().split())
data=[]
result=[[0]*m for _ in range(n)]
for i in range(n):
  data.append(list(map(int, input().split())))
for i in range(n-1,-1,-1):
  for j in range(m-1,-1,-1):
    if i==n-1 and j==m-1:
      result[i][j]=data[i][j]
    elif i==n-1:
      result[i][j]=result[i][j+1]+data[i][j]
    elif j==m-1:
      result[i][j]=result[i+1][j]+data[i][j]
    else:
      #print(i,j)
      result[i][j]=max(result[i][j+1]+data[i][j],result[i+1][j]+data[i][j])

print(result[0][0])


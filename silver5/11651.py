n=int(input())
a=[[0]*2 for _ in range(n)]

for i in range(n):
  x,y=map(int,input().split())
  a[i][0]=x
  a[i][1]=y

a.sort(key=lambda x:(x[1],x[0]))

for i in range(n):
  print(a[i][0],a[i][1])

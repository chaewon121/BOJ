n=int(input())
a=[]

for i in range(n):
  name=input().split()
  a.append((int(name[0]),name[1]))

a.sort(key=lambda x:x[0])

for i in range(n):
  print(a[i][0],a[i][1])
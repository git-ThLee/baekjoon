import sys
s=[]
a=int(sys.stdin.readline())
b=set(map(int,sys.stdin.readline().split()))
c=int(sys.stdin.readline())
d=list(map(int,sys.stdin.readline().split()))
for i in range(0,len(d)):
  if d[i] in b:
    s.append(1)
  else:
    s.append(0)
print(*s)
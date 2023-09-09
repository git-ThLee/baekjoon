n,m=map(int,input().split())
a=[]
s=list(map(int,input().split()))
for i in range(0,n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if s[i]+s[j]+s[k]>m:
        continue
      else:
        a.append(s[i]+s[j]+s[k])
print(max(a))
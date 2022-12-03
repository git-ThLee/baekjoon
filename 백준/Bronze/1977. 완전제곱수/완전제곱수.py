m = int(input())
n = int(input())
k = list()
for i in range(m,n+1):
  ii = str(i ** ( 1/2 ))
  if len(ii[ii.find('.')+1:]) == 1 :
    k.append(int(i))
if len(k) > 0 :
  print(sum(k))
  print(min(k))
else:
  print(-1)
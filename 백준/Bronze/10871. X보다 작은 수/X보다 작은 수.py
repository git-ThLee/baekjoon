n , x = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in a :
  if x > i :
    ans.append(str(i))
if len(ans) > 0 :
  print(' '.join(ans))
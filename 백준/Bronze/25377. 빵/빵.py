n = int(input())
min_time = 99999
for _ in range(n):
  a,b = list(map(int,input().split()))
  if (a <= b) and (min_time >= b) :
    min_time = b

if min_time == 99999:
  print(-1)
else:
  print(min_time)
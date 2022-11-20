h, m , s = map(int, input().split())
time = int(input())

h += time // 3600 
time = time % 3600
m += time // 60
time = time % 60
s += time 
while s > 59 :
  s -= 60
  m += 1 
while m > 59 :
  m -= 60
  h += 1
while h > 23 :
  h -= 24
print(h,m,s)
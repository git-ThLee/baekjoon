case = int(input())
a_s , b_s = 100, 100
for _ in range(case):
  a, b =map(int,input().split())
  if a > b :
    b_s -= a 
  elif a < b :
    a_s -= b
print(a_s)
print(b_s)
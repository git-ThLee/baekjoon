case = int(input())
Q = [0,0,0,0,0]
for _ in range(case):
  a , b = map(int,input().split())
  if a == 0  or b == 0 :
    Q[-1] += 1
  else :
    if a > 0 : 
      if b > 0 :
        Q[0] += 1
      elif b < 0 :
        Q[3] += 1
    elif a < 0 :
      if b > 0 :
        Q[1] += 1
      elif b < 0 :
        Q[2] += 1
print('Q1:',Q[-5])
print('Q2:',Q[-4])
print('Q3:',Q[-3])
print('Q4:',Q[-2])
print('AXIS:',Q[-1])
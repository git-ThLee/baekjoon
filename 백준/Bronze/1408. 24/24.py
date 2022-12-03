now = input().replace('\n','')
now_h = int(now[:2])
now_m = int(now[3:5])
now_s = int(now[-2:])
start = input().replace('\n','')
start_h = int(start[:2])
start_m = int(start[3:5])
start_s = int(start[-2:])

if start_s - now_s < 0 :
  if start_m == 0 :
    if start_h == 0 :
      start_h = 23
    else:
      start_h -= 1 
    start_m = 59
  else :
    start_m -= 1 
  start_s += 60
start_s -= now_s

if start_m - now_m < 0 :
  if start_h == 0 :
    start_h = 23
  else:
    start_h -= 1 
  start_m += 60
start_m -= now_m
if start_h - now_h < 0 : 
  start_h += 24
start_h -= now_h

if start_h < 10 :
  print('0'+ str(start_h),end=":")
else:
  print(str(start_h),end=":")

if start_m < 10 :
  print('0'+ str(start_m),end=":")
else:
  print(str(start_m),end=":")

if start_s < 10 :
  print('0'+ str(start_s))
else:
  print(str(start_s))
time = int(input())
button = [0,0,0]
button[0] += time // 300
time %= 300
button[1] += time // 60
time %= 60
button[2] += time // 10 
time %= 10 
if time == 0 :
  print(button[0],button[1],button[2])
else :
  print(-1)
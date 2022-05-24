now_h,now_m = map(int,input().split()) 
time_m = int(input())
now_m = now_m + time_m
for i in range(now_m // 60):
    now_h += 1
    now_m -= 60
if now_h // 24 > 0:
    now_h = now_h % 24

print(now_h,now_m)
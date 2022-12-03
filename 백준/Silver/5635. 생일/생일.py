case = int(input())
peoples = dict()
for _ in range(case):
  name , dd , mm , yy = map(str,input().split())
  if len(mm) == 1 :
    mm = '0' + mm
  if len(dd) == 1 :
    dd = '0' + dd
  y_d_m = f'{yy}-{mm}-{dd}'
  peoples[name] = y_d_m
ans = sorted(peoples.items(), key=lambda x : x[1])
print(ans[-1][0])
print(ans[0][0])
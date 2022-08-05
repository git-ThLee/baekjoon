a = list(map(int, input().split()))

ascending = True
descending = True

for i in range(1,len(a)):
  if a[i] < a[i-1] : # 이전 것이 더 크면
    ascending = False 
  else :
    descending = False

if ascending:
  print("ascending")
elif descending :
  print("descending")
else:
  print("mixed")
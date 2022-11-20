case = int(input())
for _ in range(case):
  schools = int(input())
  b_s , b_c = '', 0
  for _ in range(schools):
    school , cnt = map(str, input().split())
    if b_c <= int(cnt) :
      b_s = school
      b_c = int(cnt)
  print(b_s)
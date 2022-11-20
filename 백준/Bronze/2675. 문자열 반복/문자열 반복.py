case = int(input())
for _ in range(case) :
  num , text = map(str, input().split())
  for i in text :
    print(i*int(num) , end ="")
  print()
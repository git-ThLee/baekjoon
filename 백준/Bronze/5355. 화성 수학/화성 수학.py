case = int(input())
for _ in range(case) :
  input_ = list(map(str, input().split()))
  num = float(input_.pop(0))
  for i in input_ :
    if i == "@" :
      num *= 3
    elif i == "%":
      num += 5
    elif i == "#" :
      num -= 7
  print(f'{num:.2f}')
case = int(input())

for _ in range(case):
  input_str = input().strip()
  pw_left = []
  pw_right = []
  for i in input_str:
    if i == "<" : 
      if pw_left:
        pw_right.append(pw_left.pop())
    elif i == ">" : 
      if pw_right:
        pw_left.append(pw_right.pop())
    elif i == "-" :
      if pw_left:
        pw_left.pop()
    else:
      pw_left.append(i)
  print(''.join(pw_left) + ''.join(reversed(pw_right)))
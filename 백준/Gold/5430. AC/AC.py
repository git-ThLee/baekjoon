from collections import deque

case = int(input())

for _ in range(case):
  cmds = input().strip()
  n = int(input())
  in_list = input().strip().replace(','," ")[1:-1]
  dq = deque(map(str,in_list.split()))

  error_ = False

  reverse_flag = 0 

  if n == 0 :
    dq = []

  for cmd in cmds:
    if cmd == "R":
      # 매번 reverse() 하지 않는 방식 사용
      reverse_flag += 1 
    elif cmd == "D":
      if len(dq) < 1:
        error_ = True
        break
      else:
        if reverse_flag % 2 == 0 : # 홀수 : 뒤집힌 상태
          dq.popleft()
        else : 
          dq.pop()
        
  if error_:
    print('error')
  else:  
    if reverse_flag % 2 == 0 : # 홀수 : 뒤집힌 상태
      print('[' + ','.join(dq) +']')
    else:
      dq.reverse()
      print('[' + ','.join(dq) +']')
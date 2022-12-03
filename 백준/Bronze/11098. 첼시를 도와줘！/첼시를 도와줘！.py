case = int(input())
for _ in range(case):
  n = int(input())
  players = dict()
  for _ in range(n):
    pay , name = map(str,input().split())
    players[name] = pay
  ans = sorted(players.items() , key= lambda x : int(x[1]))
  print(ans[-1][0])
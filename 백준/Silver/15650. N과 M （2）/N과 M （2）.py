import sys

def sol(start):
  global _list
  if len(_list) == m :
    print(*_list)
    return
  for i in range(start, n+1):
    if i not in _list:
      _list.append(i)
      sol(i+1)
      _list.pop()

n,m = map(int,sys.stdin.readline().split())
_list = []
sol(1)
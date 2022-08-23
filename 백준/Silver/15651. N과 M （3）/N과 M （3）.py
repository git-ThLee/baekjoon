import sys

def sol():
  global _list
  if len(_list) == m :
    print(*_list)
    return
  for i in range(1, n+1):
    #if i not in _list:
    if _list.count(i) <= m-1 :
      _list.append(i)
      sol()
      _list.pop()

n,m = map(int,sys.stdin.readline().split())
_list = []
sol()
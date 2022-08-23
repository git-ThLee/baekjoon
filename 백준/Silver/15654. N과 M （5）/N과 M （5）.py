import sys

def sol():
  global _list, n_list
  if len(_list) == m :
    print(*_list)
    return
  for i in range(len(n_list)):
    if n_list[i] not in _list:
      _list.append(n_list[i])
      sol()
      _list.pop()

n,m = map(int,sys.stdin.readline().split())
n_list = sorted(list(map(int,sys.stdin.readline().split())))
_list = []
sol()
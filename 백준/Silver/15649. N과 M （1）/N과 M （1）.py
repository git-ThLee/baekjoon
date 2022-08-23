import sys

def sol():
  if len(list_) == m :
    print(*list_)
    return
  for i in range(1, n + 1):
    if i not in list_:
      list_.append(i)
      sol()
      list_.pop()
  

n, m = map(int,sys.stdin.readline().split())
list_ = []
sol()
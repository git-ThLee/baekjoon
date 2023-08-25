def Rev(data):
  return int(str(data)[::-1])
x, y = map(int,input().split())
print(Rev(Rev(x) + Rev(y)))
n,m = map(int,input().split())
n_ = set()
cnt = 0 
for _ in range(n):
  n_.add(input())

for _ in range(m):
  input_ = input()
  if input_ in n_ :
    cnt += 1

print(cnt)
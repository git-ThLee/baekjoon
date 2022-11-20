case = int(input())
ans = list()
for _ in range(case):
  a , b , c = map(int,input().split())
  if a == b and b == c and c == a :
    ans.append(10000 + a * 1000)
  elif a != b and b != c and c != a :
    ans.append(100 * max(a,b,c) )
  else :
    ans.append(1000 + max(a,b,c)*100)
print(max(ans))
n = int(input())
for _ in range(n):
  scores = list(map(int,input().split()))
  scores = sorted(scores)[1:-1]
  if scores[-1] - scores[0] >= 4 :
    print('KIN')
  else:
    print(sum(scores))
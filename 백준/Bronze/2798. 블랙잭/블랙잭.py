n , m = map(int,input().split())
cards = list(map(int,input().split()))

sum = 0 
for i in range(len(cards)):
  for j in range(i+1,len(cards)):
    for k in range(j+1,len(cards)):
      if cards[i]+cards[j]+cards[k] <= m and cards[i]+cards[j]+cards[k] > sum:
        sum = cards[i]+cards[j]+cards[k]

print(sum)
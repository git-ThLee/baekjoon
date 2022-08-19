import sys
import heapq

n = int(sys.stdin.readline())
hq = []
heapq.heapify(hq)

for _ in range(n):
  list_ = list(map(int,input().split()))
  for i in list_:
    if len(hq) < n :
      heapq.heappush(hq,i)
    else:
      heapq.heappushpop(hq, i)

print(min(hq))
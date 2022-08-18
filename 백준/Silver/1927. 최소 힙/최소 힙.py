import heapq
import sys

n = int(input())
hq = []
heapq.heapify(hq)

for _ in range(n):
  data = int(sys.stdin.readline())
  if data == 0 :
    if len(hq) == 0 :
      print(0)
    else:
      print(heapq.heappop(hq))
  else:
    heapq.heappush(hq,data)
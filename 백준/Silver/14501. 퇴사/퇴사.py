import sys
def sol(day, money):
  global result
  if day == n :# n에 알맞게 도착했을 때, 정답이 될 수 있다.
    result = max(result, money)
    return
  if day > n :# n을 초과한다면 범위 안에 일을 못끝내므로, 정답이 될 수 없다.
    return
  sol(day + 1 , money ) # 이번 day는 일을 하지 않고 그냥 넘어감!
  sol(day + works[day][0], money + works[day][1]) # 이번 day일을 처리함. 기간도 점프!

n = int(sys.stdin.readline())
works = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = -1 
sol(0,0)
print(result)
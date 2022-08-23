import sys

n , m , b = map(int,sys.stdin.readline().split())
tiles = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
time_result = 1000000000
floor_result = 0

for target in range(257):
  time = 0
  floor = target
  take_block = 0
  use_block = 0

  for i in range(len(tiles)):
    for j in range(len(tiles[i])):
      if tiles[i][j] != target :
        if tiles[i][j] > target : 
          take_block += tiles[i][j] - target
          #time += 2 * (tiles[i][j] - target)
        else : 
          use_block += target - tiles[i][j] 
          #time += 1 * (target - tiles[i][j])
  if use_block > take_block + b :
    continue
  time = 2 * take_block + use_block
  if time <= time_result:
    time_result = time
    floor_result = floor 

print(time_result, floor_result)
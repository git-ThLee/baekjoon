n = int(input())
key_list = list(map(int, input().split()))
m = int(input())
target_list = list(map(int, input().split()))

pool ={}
for p in key_list:
  pool[p] = 1

for i in target_list:
  if i in pool:
    print("1")
  else:
    print("0")
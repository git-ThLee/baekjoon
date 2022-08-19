import sys

case = int(sys.stdin.readline())
for _ in range(case):
  m = int(sys.stdin.readline())
  center_list = []
  median_list = []
  # 데이터 입력 
  for _ in range(m//10 + 1):
    element = list(map(int,input().split()))
    center_list += element
  #print(center_list)

  for i, v in enumerate(center_list):
    if i % 2 == 0 : # 홀수일 때
      idx = len(center_list[:i+1])//2
      median_list.append(sorted(center_list[:i+1])[idx])
  
  # 출력
  print(len(median_list))
  for i in range(len(median_list)//10 + 1):
    i += 1
    if len(median_list)//10 + 1 == i : # 10개가 안될 수도 있는 줄
      for j in median_list[10*(i-1) : (10*i) + len(median_list)%10 +1]:
        print(j,end=" ")
    else: # 10개씩 나오는 줄
      for j in median_list[10*(i-1) : (10*i)]:
        print(j,end=" ")
      print("")
  print("")
import sys

#sys.stdin=open("4344.txt","r")
#input=sys.stdin.readline

c = int(input())

for i in range(c):
  input_list = list(map(int, input().split()))
  n = input_list[0]
  n_list = input_list[1:]
  avg = sum(n_list) / len(n_list)
  
  count_student = 0
  
  for j in n_list:
    if avg < j :
      count_student += 1

  print(f'{count_student/n*100:0.3f}%' )
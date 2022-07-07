n = int(input())
p_list = list(map(int,input().split()))

sum_ = 0 
answer = 0
p_list.sort()


for i in p_list :
  sum_ += i
  answer += sum_
print(answer)
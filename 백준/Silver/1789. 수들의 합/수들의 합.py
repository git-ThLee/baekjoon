n = int(input())
sum_ = 0
i = 0
while True :
  i += 1 
  if sum_ + i > n :
    break
  sum_ += i
  
print(i-1)
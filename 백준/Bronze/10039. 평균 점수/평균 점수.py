mean_ = 0 
for _ in range(5):
  b = int(input())
  if b < 40 :
    b = 40
  mean_ += b
print(int(mean_/5))
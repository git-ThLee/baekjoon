n = int(input())
a = [i+1 for i in range(n)]

while True:
  if len(a) <= 1 :
    break
  
  a = a[1::2]
print(a[0])
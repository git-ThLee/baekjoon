m = int(input())
a = [0,1]
while m > 1  :
  m -= 1 
  a.append(sum(a[-2:]))
print(a[-1])
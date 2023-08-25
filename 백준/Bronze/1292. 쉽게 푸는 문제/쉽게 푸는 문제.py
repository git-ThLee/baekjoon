a, b = map(int,input().split())
i = 1
while True :
  r =  ','.join([ ','.join([str(j)] * j) for j in range(1,i+1)]).split(',')
  i += 1
  if b <= len(r) :
    break
print(sum([ int(i) for i in r[a-1:b]]))
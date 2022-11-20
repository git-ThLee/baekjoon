while True:
  a = int(input())
  if a == -1 :
    break
  b = list() # 모든 약수
  for i in range(1,a):
    if a % i == 0 :
      b.append(i)
  if sum(b) == a :
    print(f'{a} =' , end="")
    for i in b :
      print(f' {i} ', end='')
      if i != max(b) :
        print('+' , end ='')
    print()
  else : 
    print(f'{a} is NOT perfect.')
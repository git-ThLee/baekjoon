n = int(input())
alpa = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
for _ in range(n):
  a , b = map(str,input().split())
  print('Distances:', end=' ')
  for aa, bb in zip(a,b):
    x = alpa.index(aa.lower())
    y = alpa.index(bb.lower())
    if x - y > 0 :
      print( abs((y+26)-x) , end=' ')
    else:
      print( abs(x-y), end=' ')
  print()
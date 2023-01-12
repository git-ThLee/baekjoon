t = int(input())
for _ in range(t):
  l = input().strip()
  l_st , r_st = list() , list()
  '''
  [A,B] cur [C,D]
  [1,2,3,4]
  [1,2,3] cur [4]
  [1,2] cur [4,3]
  '''
  for i in l :
    if i == '<' :
      if len(l_st) > 0 :
        r_st.append(l_st.pop())
    elif i == '>' : 
      if len(r_st) > 0:
        l_st.append(r_st.pop())
    elif i == '-' :
      if len(l_st) > 0 :
        l_st.pop()
    else:
        l_st.append(i)
  print(''.join(l_st) + ''.join(reversed(r_st)))
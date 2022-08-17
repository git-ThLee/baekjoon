n, p  = map(int,input().split())
dict_ = dict()
cnt = 0 

for _ in range(n):
  i,j = map(int,input().split())
  if i not in dict_.keys():# 키가 없다면
    dict_[i] = []
    dict_[i].append(j)
    cnt += 1
  else:
    if max(dict_[i]) > j :
      while len(dict_[i]) > 0:
        if max(dict_[i]) <= j :
          break
        else:
          max_value = max(dict_[i])
          dict_[i].remove(max_value)
          cnt += 1
    if j not in dict_[i] :
      dict_[i].append(j)
      cnt += 1
print(cnt)
case = int(input())

for i in range(case):
  n , m = map(int, input().split())
  docs_list = list(map(int,input().split()))
  count = 1

  while 1 :
    if max(docs_list) == docs_list[0]:
      if m == 0 :
        print(count)
        break
      else:
        count += 1
        docs_list[0] = -1
    else:
      if m == 0 :
        m = len(docs_list) -1 
      else:
        m -= 1
      docs_list.append(docs_list.pop(0))
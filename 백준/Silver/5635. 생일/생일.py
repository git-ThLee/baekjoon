n = int(input())
mans = list()
for _ in range(n):
  name , day , month , year = map(str,input().split())
  mans.append({
      'name' : name,
      'year' : int(year),
      'month' : int(month),
      'day' : int(day),
  })
  mans = sorted(mans, key = lambda x : (x['year'],x['month'],x['day']))
print(mans[-1]['name'])
print(mans[0]['name'])
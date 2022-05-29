n = int(input()) # 회의 수
n_list = []
count = 0 
for i in range(n):
    start, end = map(int,input().split())
    n_list.append([start,end])
n_list.sort(key=lambda x : (x[1],x[0]))
now = 0
for i in n_list:
    if i[0] >= now :
        count += 1
        now = i[1]
print(count)
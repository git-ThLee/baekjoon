n , k  = map(int, input().split())
n_list = []
count = 0
for i in range(n):
    n_list.append(int(input())) # 동전 종류 채우기
n_list.sort(reverse=True) # 동전 큰거부터 나오기 위해 역정렬
for i in range(len(n_list)):
    if n_list[i] <= k :
        count += k // n_list[i]
        k = k % n_list[i]
        #print('동전:',n_list[i],'/ 누적 개수 :',count,'/ 남은 돈 :',k)
    if k == 0 :
        break
print(count)  
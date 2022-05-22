
k = int(input())
money_list = []
for i in range(k):
    n = int(input())
    if n == 0 :
        money_list.pop()
    else:
        money_list.append(n)
print(sum(money_list))
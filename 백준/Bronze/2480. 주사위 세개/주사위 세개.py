n = list(map(int, input().split()))
reward = 0
if n.count(n[0]) == 3:
    reward = 10000 + n[0] * 1000
elif n.count(n[0]) == 2:
    reward = 1000 + n[0] * 100
elif n.count(n[0]) == 1:
    if n[1] == n[2]:
        reward = 1000 + n[1] * 100
    else :
        reward = max(n) * 100
print(reward)
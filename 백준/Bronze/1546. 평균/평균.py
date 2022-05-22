import sys
#sys.stdin = open('input.txt', 'r')
#input=sys.stdin.readline

n = map(int, input().split())
n_list =  list(map(int, input().split()))
m = max(n_list)
for i in range(len(n_list)):
    n_list[i] = n_list[i]/m * 100

print(sum(n_list) / len(n_list))
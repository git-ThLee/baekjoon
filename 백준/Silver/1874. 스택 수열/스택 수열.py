import sys
n = int(input())
a = 0
b = []
answer = []
err = False
for _ in range(n):
    m = int(input())
    
    while a < m :
        a += 1
        b.append(a)
        answer.append('+')

    if b[-1] == m:
        b.pop()
        answer.append('-')
        
    else:
        err = True
        break

if err == True:
    print('NO')
else:
    print('\n'.join(answer))
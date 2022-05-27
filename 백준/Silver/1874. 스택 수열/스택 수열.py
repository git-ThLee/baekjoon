n = int(input())
cnt = 0
stack = []
answer = []
err = False
for _ in range(n):
    m = int(input())
    
    while cnt < m :
        cnt += 1
        stack.append(cnt)
        answer.append('+')

    if stack[-1] == m:
        stack.pop()
        answer.append('-')
        
    else:
        err = True
        break

if err == True:
    print('NO')
else:
    print('\n'.join(answer))
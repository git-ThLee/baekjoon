import sys

# 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
n = int(sys.stdin.readline())
stack1 = []
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push' :
        stack1.append(cmd[1])
    elif cmd[0] == 'pop' :
        if len(stack1) == 0 :
            print(-1)
        else:
            print(stack1.pop())
    elif cmd[0] == 'size':
        print(len(stack1))
    elif cmd[0] == 'empty':
        if len(stack1) == 0 :
            print(1)
        else:
            print(0)
    else:
        if len(stack1) == 0 :
            print(-1)
        else:
            print(stack1[-1])
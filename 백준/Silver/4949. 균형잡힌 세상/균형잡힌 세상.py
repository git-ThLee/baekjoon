# 문단 
Paragraph = ''
# 문단 모으기
while 1:
    i = str(input())
    Paragraph += i
    if i == '.':
        break
# 
for j in range(Paragraph.count('.')-1):
    # 0은 인덱스 에러 방지용
    stack1 = [0] 
    # 문장 
    sentence =  Paragraph[0:Paragraph.index('.')]
    Paragraph = Paragraph[Paragraph.index('.')+1:]
    for k in sentence:
        if k == '(':
            stack1.append('(')
        elif k == '[':
            stack1.append('[')
        elif k == ')':
            if stack1[-1] == '(':
                stack1.pop()
            else:
                stack1.append(')')
                break
        elif k == ']':
            if stack1[-1] == '[':
                stack1.pop()
            else:
                stack1.append(']')   
                break
    if len(stack1) == 1:
        print('yes')
    else:
        print('no')
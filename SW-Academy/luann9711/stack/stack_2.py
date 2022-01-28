# 테스트 케이스 입력
t = int(input('테스트 케이스 입력 : '))
c = t + 1

while t > 0:
    code = input('검사할 코드를 입력 : ')

    open_p = ['(', '[', '{']
    close_p = [')', ']', '}']
    stack = []

    for i in code:
        if i in open_p:
            stack.append(i)
            
        if i in close_p:
            stack.pop()
    
    if len(stack) == 0:
        print(f'#{c - t} {1}')
    elif len(stack) >= 1:
        print(f'#{c - t} {0}')
    
    t -= 1

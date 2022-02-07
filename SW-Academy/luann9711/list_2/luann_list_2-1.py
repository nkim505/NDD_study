# 테스트 케이스 개수 T
t = int(input('테스트 케이스 1이상 50 이하의 숫자를 입력해 주세요 : '))
c = t + 1

while t > 0:
    # 요구범위 밖의 숫자가 입력되었을때 오류메시지 출력 후 재입력
    while (t > 50) or (t <= 0):
        print('범위 밖의 숫자입니다 다시 입력해주세요')
        test_case = int(input('테스트 케이스 1이상 50 이하의 숫자를 입력해 주세요 : '))
    
    try:
        # 영역의 개수 N을 입력 받는다
        n = int(input('영역의 개수 N을 입력해 주세요 : '))
    
    except ValueError:
        print('범위 밖의 숫자입니다')
    
    # 입력범위 밖의 숫자를 입력시 ValueError 발생
    if not(2 <= n <= 30):
        raise ValueError('ValueError: WORNG NUMBER')
        exit(1)
    
    arr = [[0 for i in range(10)] for i in range(10)]
    
    
    while n > 0:
        color = list(map(int, input('범위좌표와 색상을 입력하시오 : ').split()))
        if color[-1] == 1:
            red = color[:-1]

            for i in range(red[0], red[2]+1):
                for j in range(red[1], red[3]+1):
                    arr[i][j] = 1
            red = []
            
        elif color[-1] == 2:
            blue = color[:-1]
            
            for i in range(blue[0], blue[2]+1):
                for j in range(blue[1], blue[3]+1):
                    arr[i][j] += 1
            blue = []
        
        n -= 1
    
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2:
                count += 1
    
    print(f'#{c - t} {count}')
    
    # for i in arr:
    #     print(i)
    
    t -= 1


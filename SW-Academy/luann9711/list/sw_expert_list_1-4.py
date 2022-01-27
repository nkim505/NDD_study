# 테스트 케이스 개수 T
t = int(input('테스트 케이스 1이상 50 이하의 숫자를 입력해 주세요 : '))
# 카운딩은 결과값 출력 형식에 필요한 인덱스 갑
counting = 1


# 해당 while 문은 테스트 케이스 수만큼 프로그램을 반복하기 위한 장치임
while t > 0:
    # 요구범위 밖의 숫자가 입력되었을때 오류메시지 출력 후 재입력
    while (t > 50) or (t <= 0):
        print('범위 밖의 숫자입니다 다시 입력해주세요')
        test_case = int(input('테스트 케이스 1이상 50 이하의 숫자를 입력해 주세요 : '))
    
    try:
        # 정수의 개수 N , 구간의 개수 M 입력 받는다
        n, m = map(int, input('정수의 개수 N, 구간의 개수 M을 차례대로 입력해 주세요 : ').split())
        
    except ValueError:
        print('범위 밖의 숫자입니다')
    
    # 입력범위 밖의 숫자를 입력시 ValueError 발생
    if not(10 <= n <= 100) or not(2 <= m < n):
        raise ValueError('ValueError: WORNG NUMBER')
    
    # n개의 정수 a를 list 형태로 입력받는다
    a = list(map(int, input('{}개의 숫자를 1이상 10000 이하로 입력해 주세요 : '.format(n)).split()))

    # 합계가 가장 낮고 높은 배열합을 구하기 위해 초기화된 배열합 생성
    small_sum = sum(a[0:m])
    big_sum = sum(a[0:m])
    
    # m 만큼의 범위를 설정하여 배열의 첫 요소부터 비교하여 최대합은 big_sum에
    # 최저합은 small_sum에 저장되도록 한다
    for i in range(0, (n - m + 1)):
        array_list_sum = sum(a[i:m + i])
        
        if array_list_sum >= big_sum:
            big_sum = array_list_sum
        elif array_list_sum <= small_sum:
            small_sum = array_list_sum
    
    # 최대합과 최저합의 차를 계산하여 출력한다.
    answer = big_sum - small_sum
    print(f'#{counting} {answer}')
    
    counting += 1
    t -= 1

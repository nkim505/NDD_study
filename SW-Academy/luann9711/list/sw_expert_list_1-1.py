import time

# 테스트 케이스를 입력 받는다.
test_case = int(input('테스트 케이스 1이상 50 이하의 숫자를 입력해 주세요 : '))

# 요구범위 밖의 숫자가 입력되었을때 오류메시지 출력 후 재입력
while (test_case > 50) or (test_case <= 0):
    print('범위 밖의 숫자입니다 다시 입력해주세요')
    test_case = int(input('테스트 케이스 1이상 50 이하의 숫자를 입력해 주세요 : '))

# 출력시 인덱스에 사용할 카운트 넘버
count = 1

# 프로그램 전체를 입력된 케이스 수 만큼 반복시킨다
while test_case > 0:
    # 양수의 갯수 N 을 입력 받는다.
    n = int(input('양수의 갯수를 5이상 1000이하로 입력해주세요 : '))
    
    # 요구범위 밖의 숫자가 입력되었을때 오류메시지 출력 후 재 입력
    while (n > 1000) or (n < 5):
        print('범위 밖의 숫자입니다 다시 입력해주세요')
        n = int(input('양수의 갯수를 5이상 1000이하로 입력해주세요 : '))
    
    # N 개의 양수를 입력받는다
    num = input('{}개의 양수를 입력해주세요 : '.format(n)).split()
    
    # num 으로 받은 리스트의 양수들을 숫자형으로 변환시킨다.
    for idx in range(len(num)) :
        num[idx] = int(num[idx])
    
    # 리스트에 있는 최고 값에서 최저 값을 빼서 변수 calc에 저장한다 - max(), min() 함수 사용

    # time 모듈을 사용하여 실행속도 측정
    # sorted = O(n log n)
    # min(), max() = O(n)

    start_time = time.time()
    # num = sorted(num)
    # calc = num[-1] - num[0]
    calc = max(num) - min(num)
    end_time = time.time()

    print('max - min 실행시간 {} 초'.format(end_time - start_time))
    

    # calc 의 결과 값을 인덱스와 함께 정해진 형식으로 출력한다.
    print(f'#{count} {calc}')
    
    # 남은 테스트 케이스 숫자를 1 감소시킨다
    # 남은 테스트 케이스가 0이 되면 while 문에 의해 자동으로 종료됨
    test_case -= 1
    # 인덱스에 사용할 카운트 넘버를 상승시킨다
    count += 1
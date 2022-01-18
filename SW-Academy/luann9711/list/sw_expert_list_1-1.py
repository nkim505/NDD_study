# 테스트 케이스 입력받기
test_case = int(input('테스트 케이스 1이상 50 이하의 숫자를 입력해 주세요 : '))

# 요구범위 밖의 숫자가 입력되었을때 오류메시지 출력 후 재 입력
while (test_case > 50) or (test_case <= 0):
    if (test_case > 50) or (test_case <= 0):
        print('범위 밖의 숫자입니다 다시 입력해주세요')
        test_case = int(input('테스트 케이스 1이상 50 이하의 숫자를 입력해 주세요 : '))

# 결과값을 저장하는 리스트
answer = []

# 테스트 케이스가 0보다 큰 상황에서 반복시키고 0이 되면 종료시킨다
while test_case > 0:
    # 양수의 갯수 N 을 입력 받는다.
    n = int(input('양수의 갯수를 5이상 1000이하로 입력해주세요 : '))
    
    # 요구범위 밖의 숫자가 입력되었을때 오류메시지 출력 후 재 입력
    while (n > 1000) or (n < 5):
        if (n > 1000) or (n < 5):
            print('범위 밖의 숫자입니다 다시 입력해주세요')
            n = int(input('양수의 갯수를 5이상 1000이하로 입력해주세요 : '))

    # N 개의 양수를 입력받는다
    num = input('{}개의 양수를 입력해주세요 : '.format(n)).split()
    
    # num 으로 받은 리스트의 양수들을 숫자형으로 변환시킨다.
    for idx in range(len(num)) :
        num[idx] = int(num[idx])
    
    # 리스트에 있는 최고 값에서 최저 값을 빼서 변수 calc에 저장한다 - max(), min() 함수 사용
    calc = max(num) - min(num)
    # calc 의 결과 값을 외부 list answer에 추가해 준다
    answer.append(calc)
    
    # 남은 테스트 케이스 숫자를 1 감소시킨다
    test_case -= 1
    
# answer list 에 저장된 요소들은 enumerate() 함수로 인덱스를 붙여 차례대로 출력해준다
for idx, ans in enumerate(answer, start=1):
    print('#',idx, ans)
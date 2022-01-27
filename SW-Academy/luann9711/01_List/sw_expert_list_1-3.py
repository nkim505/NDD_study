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

    # 카드 장수 n
    n = int(input('카드 장수 5이상 100 이하의 숫자를 입력해 주세요 : '))

    # 요구범위 밖의 숫자가 입력되었을때 오류메시지 출력 후 재입력
    while (n > 100) or (n < 5):
        print('범위 밖의 숫자입니다 다시 입력해주세요')
        test_case = int(input('카드 장수 5이상 100 이하의 숫자를 입력해 주세요 : '))

    # n개의 숫자를 입력받은 리스트 a
    a = list(map(int, input('{}개의 숫자를 0이상 9 이하로 입력해 주세요 : '.format(n).strip())))


    # 요구범위 밖의 숫자가 입력되었을때 오류메시지 출력 후 재입력
    # while (n > 9) or (n < 0):
    #     print('범위 밖의 숫자입니다 다시 입력해주세요')
    #     test_case = int(input('{}개의 숫자를 0이상 9 이하로 입력해 주세요 : '.format(n)))



    # 리스트 안에서 각 요소들의 갯수를 센다
    # 각 숫자와 각 숫자의 갯수를 저장할 딕셔너리를 생성한다
    new_alist = {}
    # 딕셔너리에서 추출된 키들의 리스트
    keylist = []
    # 딕셔너리에서 추출된 값들의 리스트
    valuelist = []

    # 딕셔너리에 각 요소들의 중복 값을 저장한다
    for i in a:
        try: new_alist[i] += 1
        except: new_alist[i] = 1
    
    # 딕셔너리에서 키과 값을들 분리해 추출하여 각각 저장한다
    for i in new_alist:
        keylist.append(i)
        valuelist.append(new_alist[i])
    
    # 값들의 리스트 중 최고값을 구해서 그 인덱스를 변수 maxvalueindex 에 저장한다
    maxvalueindex = valuelist.index(max(valuelist))
    
    # 값들이 모두 같을 경우 숫자가 가장 큰 키의 인덱스를 maxvalueindex에 저장한다
    if max(valuelist) == min(valuelist):
        maxvalueindex = keylist.index(max(keylist))
    
    # 각 리스트들에서 maxvalueindex 에 저장된 인덱스의 요소들을 변수에 저장한다.
    maxkey = keylist[maxvalueindex]
    maxvalue = valuelist[maxvalueindex]

    print('#{} {} {}'.format(counting, maxkey, maxvalue))
    
    counting += 1
    t -= 1







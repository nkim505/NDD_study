# 테스트 케이스 입력받기
test_case = int(input())
# 인덱스 숫자 카운팅
counting = 1
answer = []

while test_case > 0:
    num_split = int(input())
    num = input().split()

    for idx in range(len(num)) :
        num[idx] = int(num[idx])

    num = sorted(num)
    calc = num[-1] - num[0]

    print('#{}'.format(counting), calc)

    test_case -= 1
    counting += 1



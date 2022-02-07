# 테스트 케이스 입력
try:
    t = int(input('테스트 케이스 입력 : '))
except ValueError:
    print('ValueError : Wrong Number!!')
if not(1 <= t <= 50):
    raise ValueError

c = t + 1

def check_word(check_list):
        for idx in range(len(check_list)):
            if idx >= len(check_list) - 1:
                break

            if check_list[idx] == check_list[idx + 1]:
                del check_list[idx + 1], check_list[idx]
                check_word(check_list)
        return len(check_list)

while t > 0:
    try:
        a = input('길이가 1000이내인 문자열을 입력 : ')
    except ValueError:
        print('ValueError : Wrong length of word!!')
    if not(1 <= len(a) <= 1000):
        raise ValueError

    a_list = []

    for i in a:
        a_list.append(i)

    print(f'#{c - t} {check_word(a_list)}')

    t -= 1
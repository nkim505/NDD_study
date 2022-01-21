# List 1 - 8th -number card
#  0-9 N card
try:
    T = int(input('Type test case number (T) between 1 and 50'))
except ValueError:
    print('Type positive integer')
if not (1 <= T <= 50):
    raise ValueError('T should be 1 <= T <= 50')
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    try:
        N = int(input('Type number of card N (5 <= N <= 100'))
    except ValueError:
        print('Type positive integer')
    if not (5 <= N <= 100):
        raise ValueError('N should be 5 <= N <= 100')
    try:
        card_str = input('Type N numbers without space')
        card_numbers = [int(card_str[idx]) for idx in range(0, len(card_str))]
    except ValueError:
        print('Type only numbers without space')
    if len(card_numbers) != N:
        raise ValueError(f'Type {N} numbers without space')
    # count numbers either use 'unique' or just count it.
    # two array # unique card and card -numbers
    unique_number = []
    number_count = []
    most_freq_card_num = 0
    most_freq_val = 0
    for idx in range(0, len(card_str)):
        if card_numbers[idx] not in unique_number:
            unique_number.append(int(card_str[idx]))
            number_count.append(card_numbers.count(card_numbers[idx]))
    most_freq_val = unique_number[0]
    most_freq_num = number_count[0]
    for idx2 in range(1, len(unique_number)):
        if most_freq_num < number_count[idx2]:
            most_freq_num = number_count[idx2]
            most_freq_val = unique_number[idx2]
        elif most_freq_num == number_count[idx2]:
            if most_freq_val < unique_number[idx2]:
                most_freq_val = unique_number[idx2]
                most_freq_num = number_count[idx2]
    print(f'#[test case] [most frequent value] [most frequent card number]')
    print(f"#{test_case} {most_freq_val} {most_freq_num}")

# List1-9th-local_sum difference
try:
    T = int(input('Type test case number (T) between 1 and 50'))
except ValueError:
    print('Type positive integer')
if not (1 <= T <= 50):
    raise ValueError('T should be 1 <= T <= 50')
for test_case in range(1, T + 1):
    try:
        N, M = map(int, input('Type number of integer (N) \
            and number of section(M)').split())
    except ValueError:
        print('Type two integers should be separated by whitespace')
    if not (10 <= N <= 100) or not (2 <= M <= N):
        raise ValueError('Check range: (10 <= N <= 100) and ( 2 <= M <= N)')
    try:
        num_list = list(map(int, input(f'Type {N}integers \
                separated by whitespace,1<=each integer<=10000').split()))
    except ValueError:
        print('Type only integers separated by whitespace')
    if len(num_list) != N:
        raise ValueError(f'Value Error:type {N} integers')
    if not all(1 <= input_int <= 10000 for input_int in num_list):
        raise ValueError('Check input integer range: 1<=each integer<=10000')
    tmp_max = sum(num_list[0:M])
    tmp_min = sum(num_list[0:M])
    for idx2 in range(1, N-M+1):
        tmp_sum = sum(num_list[idx2:idx2+M])
        if tmp_sum > tmp_max:
            tmp_max = tmp_sum
        elif tmp_sum < tmp_min:
            tmp_min = tmp_sum
    diff = tmp_max-tmp_min
    print("#[test case number] [maximum difference between section sum]")
    print(f"#{test_case} {diff}")

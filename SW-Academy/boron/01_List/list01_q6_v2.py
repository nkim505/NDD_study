# List1-6th-min max problem -reflect feedbacks
T = int(input('Type test case number (T)'))
if T < 1:
    raise ValueError('T should be a positive integer')
for test_case in range(1, T + 1):
    try:
        N = int(input('Type test sample size (N), 5<=N<=1000'))
    except ValueError:
        print('ValueError: N should be an integer')
    if not (5 <= N <= 1000):
        raise ValueError(f'N should be between 5 and 1000, not {N}')
    print('Type N positive integers separated by whitespace')
    try:
        input_number_array = list(map(int, input().split()))
    except ValueError:
        print(f'ValueError:Type {N} positive integers separated by whitespace')
    if len(input_number_array) != N:
        raise ValueError('Input array size is not '+str(N))
    tmp_smallest = input_number_array[0]
    tmp_largest = input_number_array[0]
    for test_number_index in range(1, N):
        if input_number_array[test_number_index] < tmp_smallest:
            tmp_smallest = input_number_array[test_number_index]
        elif input_number_array[test_number_index] > tmp_largest:
            tmp_largest = input_number_array[test_number_index]
    print('Print output: #[Test number] [max-min]')
    print(f"#{test_case} {tmp_largest-tmp_smallest}")

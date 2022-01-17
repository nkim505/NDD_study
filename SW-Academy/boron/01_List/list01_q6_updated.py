# List1-6th-min max problem
print('Type test case number (T)')
T = int(input())
if T < 1:
    raise ValueError('T should be a positive integer')
for test_case in range(1, T + 1):
    print('Type test sample size (N), N is a integer and 5<=N<=1000')
    N = int(input())
    if (N < 5) or (N > 1000):
        raise ValueError('N should be between 5 and 1000')
    print('Type N positive integers separated by whitespace')
    input_number_array = list(map(int, input().split()))
    if len(input_number_array) != N:
        raise ValueError('Input array size is not '+str(N))
    tmp_smallest = input_number_array[0]
    tmp_largest = input_number_array[0]
    for test_number_index in range(1, N):
        if input_number_array[test_number_index] < tmp_smallest:
            tmp_smallest = input_number_array[test_number_index]
        elif input_number_array[test_number_index] > tmp_largest:
            tmp_largest = input_number_array[test_number_index]
    print('Print output: #Test number max-min')
    print("#"+str(test_case)+' '+str(tmp_largest-tmp_smallest))

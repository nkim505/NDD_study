# List2- 8th-sorting
try:
    T = int(input('Type test case number (T) between 1 and 50'))
except ValueError:
    print('Type positive integer')
if not (1 <= T <= 50):
    raise ValueError('T should be 1 <= T <= 50')
for test_case in range(1, T + 1):
    try:
        N = int(input('Type Number of integer (10<=N<=100)'))
    except ValueError:
        print('Type only positive integer')
    if not (10 <= N <= 100):
        raise ValueError('ValueError, check range - 10<=N<=100')
    try:
        input_arr = list(map(int, input().split(f'Type {N} integers \
            separated by white space, 1<= each integer <=100')))
    except ValueError:
        print('Type Integers and whitespace only')
    if len(input_arr) != N:
        raise ValueError(f'Number of input error:Type {N} integers!')
    if not all(1 <= input_val <= 100 for input_val in input_arr):
        raise ValueError(f'input value range error: 1<=input value<=100')
    # Actually, i need only 10 values.
    # So 1-5th min value
    # 1-5th max value (max(1),min(1))
    for idx in range(0, N-1):
        tmp_min = idx
        for idx2 in range(idx+1, N):
            if input_arr[tmp_min] > input_arr[idx2]:
                tmp_min = idx2
        input_arr[idx], input_arr[tmp_min] = input_arr[tmp_min], input_arr[idx]
    print_string = "#"+str(test_case)
    for print_idx in range(5):
        print_string = print_string+" "+str(input_arr[-print_idx-1])
        print_string = print_string+" "+str(input_arr[print_idx])
    print(print_string)
# Better way is probably using 'quick sort O(nlogn)

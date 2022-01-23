# List1-7th-bus stop problem
try:
    T = int(input('Type test case number (T)'))
except ValueError:
    print('Type positive integer')
if T < 1:
    raise ValueError('T should be a positive integer')
for test_case in range(1, T + 1):
    print('Type three positive integers sepearated by white space: K N M \
        \nK: charging capacity - number of bus stops without charging,\
        \nN: Total number of bus stops, \
        \nM: Number of charging stations')
    try:
        K, N, M = map(int, input().split())
    except ValueError:
        print('ValueError: Type integers separated by whitespace')
    if not all(1 <= set_val <= 100 for set_val in [K, N, M]):
        raise ValueError('All input should be between 1 and 100')
    if M > N:
        raise ValueError('M <= N')
    try:
        charging_stop = list(map(int, input('Type charging station bus stop \
            numbers seperated by whitespace').split()))
    except ValueError:
        print('ValueError: Type integers separated by whitespace')
    if len(charging_stop) != M:
        raise ValueError(f'Input array size should be {M}')
    current_stop = 0
    charging_number = 0
    next_charging_idx = 0
    while current_stop < N:
        # If cur+K => N then we don't need to charge, so end
        if ((current_stop + K) >= N):
            print(f"#{test_case} {charging_number}")
            break
        else:
            # If there is no available next charging stop
            # (next charging stop index= M, if we increment it by 1)
            if next_charging_idx >= (M):
                # Fail to arrive terminal stop
                print(f"#{test_case} 0")
                break
            else:
                # there is available charing stop.
                if current_stop + K < charging_stop[next_charging_idx]:
                    # it cannot arrive so fail.
                    print(f"#{test_case} 0")
                    break
                else:
                    # Now I need to find 'minimum number'
                    # so find the maximum charging stop number satisfying
                    # "current_Stop_number+K >= nextcharging stop number"
                    charging_number = charging_number+1
                    while current_stop + K >= charging_stop[next_charging_idx]:
                        if next_charging_idx == M-1:
                            # this is when first trial was the last stop
                            next_charging_idx = next_charging_idx + 1
                            break
                        else:
                            # next_charging_stop_index<M-1
                            next_charging_idx = next_charging_idx + 1
                    current_stop = charging_stop[next_charging_idx-1]

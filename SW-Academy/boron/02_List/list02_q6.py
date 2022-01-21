# List2- 6th - subset sum
try:
    T = int(input('Type test case number (T) between 1 and 50'))
except ValueError:
    print('Type positive integer')
if not (1 <= T <= 50):
    raise ValueError('T should be 1 <= T <= 50')
for test_case in range(1, T + 1):
    arr = list(range(1, 13))
    count = 0
    try:
        N, K = map(int, input('Type size of subset (N) \
            and sum of subset (K) separated by whitespace').split())
    except ValueError:
        print('Type two integers separated by whitespace')
    if not (1 <= N <= 12) or not (1 <= K <= 100):
        raise ValueError('Check range: 1 <= N <= 12) and (1 <= K <= 100')
    for subset_idx in range(1 << 12):
        tmp_subset = []
        for index in range(12):
            if subset_idx & (1 << index):
                tmp_subset.append(arr[index])
        if (len(tmp_subset) == N) and (sum(tmp_subset) == K):
            count = count+1
    print(f'#[Test number] [number of subset which size{N} and sum{K}]')
    print(f"#{test_case} {count}")

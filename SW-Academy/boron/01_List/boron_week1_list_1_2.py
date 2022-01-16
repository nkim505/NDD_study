# List1-6th-min max problem
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    input_number_array = []
    input_number_array = list(map(int, input().split()))
    tmp_smallest = input_number_array[0]
    tmp_largest = input_number_array[0]
    for test_number_index in range(1, N):
        if input_number_array[test_number_index] < tmp_smallest:
            tmp_smallest = input_number_array[test_number_index]
        elif input_number_array[test_number_index] > tmp_largest:
            tmp_largest = input_number_array[test_number_index]
    print("#"+str(test_case)+' '+str(tmp_largest-tmp_smallest))

# List1-7th-bus stop problem

T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charging_stop = list(map(int, input().split()))
    current_stop = 0
    charging_number = 0
    next_charging_idx = 0
    while current_stop < N:
        if ((current_stop + K) >= N):
            print("#"+str(test_case)+' '+str(charging_number))
            break
        else:
            if next_charging_idx >= (M):
                print("#"+str(test_case)+' '+str(0))
                break
            else:
                if current_stop + K < charging_stop[next_charging_idx]:
                    print("#"+str(test_case)+' '+str(0))
                    break
                else:
                    charging_number = charging_number+1
                    while current_stop + K >= charging_stop[next_charging_idx]:
                        if next_charging_idx == M-1:
                            next_charging_idx = next_charging_idx + 1
                            break
                        else:
                            next_charging_idx = next_charging_idx + 1
                    current_stop = charging_stop[next_charging_idx-1]
# List 1 - 8th -number card
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    card_str = input()
    card_numbers = [int(card_str[idx]) for idx in range(0, len(card_str))]
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
    print("#"+str(test_case)+" "+str(most_freq_val)+" "+str(most_freq_num))
# List1-9th-local_sum difference
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    tmp_max = sum(num_list[0:M])
    tmp_min = sum(num_list[0:M])
    for idx2 in range(1, N-M+1):
        tmp_sum = sum(num_list[idx2:idx2+M])
        if tmp_sum > tmp_max:
            tmp_max = tmp_sum
        elif tmp_sum < tmp_min:
            tmp_min = tmp_sum
    diff = tmp_max-tmp_min
    print("#"+str(test_case)+" "+str(diff))
# List2-5th-count_purple
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    colored_path_idx = []
    colored_patch_color = []
    for num_area in range(N):
        r1, c1, r2, c2, pcolor = map(int, input().split())
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if [row, col] not in colored_path_idx:
                    colored_path_idx.append([row, col])
                    colored_patch_color.append(pcolor)
                else:
                    exist_idx = colored_path_idx.index([row, col])
                    if colored_patch_color[exist_idx] != 3:
                        if colored_patch_color[exist_idx] != pcolor:
                            colored_patch_color[exist_idx] = 3
    purple = 0
    for count in range(len(colored_patch_color)):
        if colored_patch_color[count] == 3:
            purple = purple+1
    print("#"+str(test_case)+" "+str(purple))
# List2- 6th - subset sum
T = int(input())
for test_case in range(1, T + 1):
    arr = list(range(1, 13))
    count = 0
    N, K = map(int, input().split())
    for subset_idx in range(1 << 12):
        tmp_subset = []
        for index in range(12):
            if subset_idx & (1 << index):
                tmp_subset.append(arr[index])
        if (len(tmp_subset) == N) and (sum(tmp_subset) == K):
            count = count+1
    print("#"+str(test_case)+" "+str(count))
# List 2- 7th - binary search


def binary_search(start_pg, end_pg, goal_pg):
    search_num = 0
    while start_pg <= end_pg:
        search_num = search_num+1
        mid_pg = int((start_pg+end_pg)/2)
        if goal_pg < mid_pg:
            end_pg = mid_pg
        elif goal_pg > mid_pg:
            start_pg = mid_pg
        else:
            break
    return search_num


T = int(input())
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    asearch = binary_search(1, P, Pa)
    bsearch = binary_search(1, P, Pb)
    if asearch > bsearch:
        winner = 'B'
    elif asearch < bsearch:
        winner = 'A'
    else:
        winner = 0
    print("#"+str(test_case)+" "+str(winner))

# List2- 8th-sorting
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    input_arr = list(map(int, input().split()))
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
# It works but this version did not really use 'sorting'
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    input_arr = list(map(int, input().split()))
    sorted_arr = []
    while(len(sorted_arr) < N):
        max_idx = input_arr.index(max(input_arr))
        min_idx = input_arr.index(min(input_arr))
        if max_idx != min_idx:
            sorted_arr.append(max(input_arr))
            sorted_arr.append(min(input_arr))
            input_arr.remove(max(input_arr))
            input_arr.remove(min(input_arr))
        else:
            sorted_arr.append(max(input_arr))
            input_arr.remove(max(input_arr))
            break
    print_string = "#"+str(test_case)
    for idx in range(10):
        print_string = print_string+" "+str(sorted_arr[idx])
    print(print_string)

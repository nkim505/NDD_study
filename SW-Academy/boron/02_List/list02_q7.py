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


try:
    T = int(input('Type test case number (T) between 1 and 50'))
except ValueError:
    print('Type positive integer')
if not (1 <= T <= 50):
    raise ValueError('T should be 1 <= T <= 50')
for test_case in range(1, T + 1):
    try:
        P, Pa, Pb = map(int, input('Type whole page number[P],\
        page number for A[Pa],page number for B[Pb],\
        1<=P,Pa,Pb <=1000').split())
    except ValueError:
        print('Type three integers separated by whitespace')
    if not all(1 <= pg_num <= 1000 for pg_num in [P, Pa, Pb]):
        raise ValueError('ValueError: 1<=P,Pa,Pb <=1000')
    asearch = binary_search(1, P, Pa)
    bsearch = binary_search(1, P, Pb)
    if asearch > bsearch:
        winner = 'B'
    elif asearch < bsearch:
        winner = 'A'
    else:
        winner = 0
    print("Output: [#Test number] [Winner]")
    print(f"#{test_case} {winner}")

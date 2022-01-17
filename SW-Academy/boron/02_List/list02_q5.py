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

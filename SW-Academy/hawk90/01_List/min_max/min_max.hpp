#define MIN_SAMPLE 5
#define MAX_SAMPLE 1000

int sub_max_min_in_list(const int *array) {
    std::cout << *array << std::endl;
    int min = 0;
    int max = 0;

    // min_max

    return max - min;
}

void result_print(const int test_case_idx, const int sub) {
    std::cout << "#" << test_case_idx + 1 << ": " << sub << std::endl;
}

void test_case(const int test_case_idx) {
    int sample_size;
    int *tmp;

    std::cout << "Type test sample size (N), N is a integer and 5 <= N <= 1000 ";
    std::cin >> sample_size;
    if (MIN_SAMPLE > sample_size || sample_size < MAX_SAMPLE) {
        std::cout << "sample size: " << sample_size << std::endl;
        exit(1);
    }

    int sub = sub_max_min_in_list(tmp);
    std::cout << "#" << test_case_idx + 1 << ": " << sub << std::endl;



    result_print(test_case_idx, sub);
}

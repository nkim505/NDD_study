#include <iostream>
#include <ostream>
#include <stdexcept>

#include "./min_max.h"

int sub_max_min_in_list(const int *array) {
    int min = 0;
    int max = 0;

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
        throw std::invalid_argument("Wrong in test case");
    }

    int sub = sub_max_min_in_list(tmp);
    result_print(test_case_idx, sub);
}

int main(void) {
    int num_test_case;

    try {
        std::cout << "Type number of test case (T) ";
        std::cin >> num_test_case;
        if (1 > num_test_case) {
            throw std::invalid_argument("Wrong");
        }

        for (int i = 0; i < num_test_case; ++i) {
            test_case(i);
        }

    } catch (std::invalid_argument &e) {
        std::cerr << e.what() << std::endl;
        return -1;
    }

    return 0;
}

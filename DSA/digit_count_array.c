#include <stdio.h>

int count_digits(int n) {
    int count = 0;
    while (n != 0) {
        n /= 10;
        count++;
    }
    return count;
}

int main() {
    int arr[] = {123, 4567, 89, 0, -456};
    int n = sizeof(arr) / sizeof(arr[0]); // sizeof tell the total size of an array in bytes
                                          // but to find the actual size we divide it by the size each element is occupying

    int total_digits = 0;
    for (int i = 0; i < n; i++) {
        total_digits += count_digits(arr[i]);
    }

    printf("Total number of digits: %d\n", total_digits);

    return 0;
}

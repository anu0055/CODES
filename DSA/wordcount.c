#include <stdio.h>
#include <ctype.h>
int main() {
    char str[100];
    int word_count = 0, i;
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] == ' ' && str[i+1] != ' ') {
            word_count++;
        }
    }

    printf("Number of words in the string: %d", word_count+1);
    return 0;
}

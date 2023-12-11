#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[]) 
{
    printf("--- Day 1: Trebuchet?! ---\n");

    FILE *input_file = fopen(argv[1], "r");
    if (input_file == NULL) 
    {
        printf("Error opening file %s\n", argv[1]);
        return 1; // Error
    }

    char buffer[1024];
    uint32_t sum = 0;
    while (fgets(buffer, sizeof(buffer), input_file) != NULL) 
    {
        uint16_t left_index = 0;
        uint16_t right_index = strlen(buffer) - 1;
        uint16_t left_digit, right_digit, join;

        // Scan from the left until we find a digit
        while (buffer[left_index] && !isdigit(buffer[left_index])) 
            left_index++;

        // Scan from the right until we find a digit
        while (right_index >= 0 && !isdigit(buffer[right_index])) 
            right_index--;

        left_digit = buffer[left_index] - '0';  // Convert to integer
        right_digit = buffer[right_index] - '0';  // Convert to integer

        // If we found both digits, break out of the loop
        if (left_digit >= 0 && right_digit >= 0) 
        {
            join = left_digit * 10 + right_digit;
            printf("%s -> %d + %d = %d\n", buffer, left_digit, right_digit, join);
            sum += join;
        }
    }

    printf("Sum: %d\n", sum);
    fclose(input_file);

    return 0;
}
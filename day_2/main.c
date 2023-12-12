#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    printf("--- Day 2: Cube Conundrum ---\n");

    FILE *input_file = fopen(argv[1], "r");
    if (input_file == NULL) 
    {
        printf("Error opening file %s\n", argv[1]);
        return 1; // Error
    }

    char buffer[1024];
    int answer = 0;
    while (fgets(buffer, sizeof(buffer), input_file) != NULL) 
    {
        // Each line has this form: Game 12: 1 green, 6 red, 5 blue; 3 green, 2 red, 4 blue; 3 green, 1 red, 3 blue
        // We need to grab the game number, and test if each handful (separated by ';') is valid.
        // A handful is valid if the numbers of the cubed do not execeed: 12 red, 13 green, 14 blue.
        // If a handful is valid, we add the number of the game number to the sum.

        int game_number = 0, red = 0, green = 0, blue = 0;
        char *cursor = buffer;
        
        while (sscanf(cursor, "Game %d:", &game_number) == 1)
        {
            printf("Game number: %d\n", game_number);
            
            cursor = strchr(cursor, ':') + 1;
            while (sscanf(cursor, "%d red,", &red) == 1)
            {
                cursor = strchr(cursor, ',') + 1;
                sscanf(cursor, "%d green,", &green);
                cursor = strchr(cursor, ',') + 1;
                sscanf(cursor, "%d blue;", &blue);
                cursor = strchr(cursor, ';') + 1;
                printf("    -> Red: %d, Green: %d, Blue: %d\n", red, green, blue);
            }
            
        }

        cursor = strchr(cursor, ';') + 1;
    }

    return 0;
}
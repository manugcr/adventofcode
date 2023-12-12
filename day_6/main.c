#include <stdio.h>
#include <stdint.h>

int calculate_ways(int time, int distance)
{
    int ways = 0;
    int speed = 0;

    for (int i = 0; i < time; i++)
    {
        speed = i;
        if (speed * (time - i) > distance)
            ways++;
    }

    return ways;
}

int main (int argc, char *argv[])
{
    printf("--- Day 6: Wait For It ---\n");

    int TIMES[4]       = {50, 74, 86, 85};
    int DISTANCES[4]   = {242, 1017, 1691, 1252};
    int ways[]         = {0};
    int answer         = 1; 

    /* Calculate ways and answer */
    for (int i = 0; i < 4; i++)
    {
        ways[i] = calculate_ways(TIMES[i], DISTANCES[i]);
        printf("Ways: %d\n", ways[i]);
        answer *= ways[i];
    }

    printf("Answer: %d\n", answer);

    return 0;
}
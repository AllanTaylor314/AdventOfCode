#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    FILE* file = fopen("1.txt", "r");
    int floor = 0;
    int position = 0;
    bool above = true;
    char c;
    do {
        c = fgetc(file);
        if (c=='(') ++floor;
        if (c==')') --floor;
        if (above) ++position;
        if (floor < 0) above = false;
    } while (c != EOF);
    printf("Part 1: %d\nPart 2: %d\n", floor, position);
}

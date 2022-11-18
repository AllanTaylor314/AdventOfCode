#include <stdio.h>
#include <stdbool.h>


int main(void)
{
    FILE* file = fopen("2.txt", "r");
    int l,w,h;
    int total_area = 0;
    int total_length = 0;
    while (fscanf(file,"%dx%dx%d",&l,&w,&h)!=EOF) {
        int max = (l>w?(l>h?l:h):(w>h?w:h));
        total_area += 2*(l*w+w*h+h*l)+l*w*h/max;
        total_length += 2*(l+w+h-max)+l*w*h;
    }
    printf("Part 1: %d\nPart 2: %d\n",total_area, total_length);
}

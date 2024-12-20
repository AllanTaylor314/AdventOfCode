#include <stdio.h>

#define COORD(row,col) ((row)*lineSize+(col))
#define GRID_SIZE 40000
int grid[GRID_SIZE] = {0};

int main(void) {
    int c;
    int startIndex = -1;
    int endIndex = -1;
    int lineSize = -1;
    int numLines = 0;
    int index = 0;
    int startRow, startCol, endRow, endCol;
    while ((c = fgetc(stdin)) != EOF) {
        if (c == 'S') startIndex = index;
        if (c == 'E') endIndex = index;
        if (c == '\n') {
            ++numLines;
            if (lineSize < 0)
                lineSize = index;
        } else {
            grid[index++] = c == '#' ? -1 : 0;
        }
        if (index >= GRID_SIZE) return 1;
    }
    if (startIndex < 0 || endIndex < 0 || lineSize < 0) return 1;
    startRow = startIndex / lineSize;
    startCol = startIndex % lineSize;
    endRow = endIndex / lineSize;
    endCol = endIndex % lineSize;
    int row = startRow, col = startCol, prevRow = startRow, prevCol = startCol, pathCost = 0;
    while (row != endRow || col != endCol) {
        if ((row + 1 != prevRow || col != prevCol) && grid[COORD(row + 1,col)] >= 0) {
            prevRow = row;
            prevCol = col;
            ++row;
            grid[COORD(row,col)] = ++pathCost;
        } else if ((row - 1 != prevRow || col != prevCol) && grid[COORD(row - 1,col)] >= 0) {
            prevRow = row;
            prevCol = col;
            --row;
            grid[COORD(row,col)] = ++pathCost;
        } else if ((row != prevRow || col + 1 != prevCol) && grid[COORD(row,col + 1)] >= 0) {
            prevRow = row;
            prevCol = col;
            ++col;
            grid[COORD(row,col)] = ++pathCost;
        } else if ((row != prevRow || col - 1 != prevCol) && grid[COORD(row,col - 1)] >= 0) {
            prevRow = row;
            prevCol = col;
            --col;
            grid[COORD(row,col)] = ++pathCost;
        } else {
            return 2;
        }
    }

    int p1 = 0;
    for (int i = 1; i < numLines - 1; ++i) {
        for (int j = 1; j < lineSize - 1; ++j) {
            if (grid[COORD(i-1,j)] >= 0 && grid[COORD(i+1,j)] - grid[COORD(i-1,j)] - 2 >= 100) ++p1;
            if (grid[COORD(i+1,j)] >= 0 && grid[COORD(i-1,j)] - grid[COORD(i+1,j)] - 2 >= 100) ++p1;
            if (grid[COORD(i,j-1)] >= 0 && grid[COORD(i,j+1)] - grid[COORD(i,j-1)] - 2 >= 100) ++p1;
            if (grid[COORD(i,j+1)] >= 0 && grid[COORD(i,j-1)] - grid[COORD(i,j+1)] - 2 >= 100) ++p1;
        }
    }
    printf("Part 1: %d\n", p1);

    int p2 = 0;
    for (int i = 0; i < numLines; ++i) {
        for (int j = 0; j < lineSize; ++j) {
            if (grid[COORD(i,j)] >= 0) {
                for (int dist = 1; dist <= 20; ++dist) {
                    for (int di = 1; di <= dist; ++di) {
                        int dj = dist - di;
                        if (0 <= i+di && i+di < numLines && 0 <= j+dj && j+dj < lineSize && grid[COORD(i+di,j+dj)] >= 0 && grid[COORD(i,j)] - grid[COORD(i+di,j+dj)] - dist >= 100) ++p2;
                        if (0 <= i+dj && i+dj < numLines && 0 <= j-di && j-di < lineSize && grid[COORD(i+dj,j-di)] >= 0 && grid[COORD(i,j)] - grid[COORD(i+dj,j-di)] - dist >= 100) ++p2;
                        if (0 <= i-di && i-di < numLines && 0 <= j-dj && j-dj < lineSize && grid[COORD(i-di,j-dj)] >= 0 && grid[COORD(i,j)] - grid[COORD(i-di,j-dj)] - dist >= 100) ++p2;
                        if (0 <= i-dj && i-dj < numLines && 0 <= j+di && j+di < lineSize && grid[COORD(i-dj,j+di)] >= 0 && grid[COORD(i,j)] - grid[COORD(i-dj,j+di)] - dist >= 100) ++p2;
                    }
                }
            }
        }
    }
    printf("Part 2: %d\n", p2);
}

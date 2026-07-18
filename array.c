#include <stdio.h>

// arr is an array containing 10 arrays,
// and each of those arrays contains 10 integers.
int main(void)
{
    int arr[10][10];

    for (int row = 0; row < 10; row++)
    {
        for (int col = 0; col < 10; col++)
        {
            arr[row][col] = row * 10 + col;
        }
    }

    printf("10 x 10 Array:\n\n");

    for (int row = 0; row < 10; row++)
    {
        for (int col = 0; col < 10; col++)
        {
            printf("%3d ", arr[row][col]);
        }
        printf("\n");
    }

    return 0;
}

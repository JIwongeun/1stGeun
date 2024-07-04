#include <stdio.h>
#include <string.h>

int main() {
    char board_1[8][9] = {
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
    };

    char board_2[8][9] = {
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
    };

    int row, col;
    scanf("%d %d", &row, &col);

    char board[50][51] = {0};

    for (int i = 0; i < row; i++) {
        scanf("%s", board[i]);
    }

    int result = 64;  // 최대 칠해야 하는 개수는 64개 (8x8 체스판의 모든 칸을 다시 칠해야 할 경우)

    for (int row_start = 0; row_start <= row - 8; row_start++) {
        for (int col_start = 0; col_start <= col - 8; col_start++) {
            int count1 = 0;
            int count2 = 0;

            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    if (board[row_start + i][col_start + j] != board_1[i][j]) {
                        count1++;
                    }
                    if (board[row_start + i][col_start + j] != board_2[i][j]) {
                        count2++;
                    }
                }
            }

            // 두 경우 중에서 최소 카운트 선택
            int min_count = (count1 < count2) ? count1 : count2;

            if (result > min_count) {
                result = min_count;
            }
        }
    }

    printf("%d", result);

    return 0;
}
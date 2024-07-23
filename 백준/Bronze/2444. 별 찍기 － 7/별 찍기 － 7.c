#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    // 위쪽 피라미드 출력
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N - i; j++) {
            printf(" ");
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    // 아래쪽 피라미드 출력
    for (int i = N - 1; i >= 1; i--) {
        for (int j = 1; j <= N - i; j++) {
            printf(" ");
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
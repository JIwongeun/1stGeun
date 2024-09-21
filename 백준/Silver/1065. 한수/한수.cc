#include<iostream>

using namespace std;


int main(void) {

    int N, cnt=0;

    cin >> N;

    if (N < 100) {
        cnt= N;
    }
    else {
        cnt = 99;
        for (int i = 100; i <= N; i++) {
            int hun = i / 100;
            int ten = (i / 10) % 10;
            int one = i % 10;

            if ((hun - ten) == (ten - one)) {
                cnt++;
            }
        }
    }

    cout << cnt;

    return 0;

}

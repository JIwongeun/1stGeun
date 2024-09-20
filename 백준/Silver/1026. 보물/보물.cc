#include<iostream>
#include<algorithm>

using namespace std;


bool comp(int a, int b) {
    return a > b;
}

int main(void) {
       
    int A[51], B[51];

    int N;

    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < N; i++) {
        cin >> B[i];
    }

    sort(A, A+N);
    sort(B, B + N, comp);

    int result = 0;

    for (int i = 0; i < N; i++) {
        result += A[i] * B[i];
    }

    cout << result << endl;

}

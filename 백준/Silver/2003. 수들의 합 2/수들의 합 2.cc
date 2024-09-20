#include<iostream>
#include<algorithm>

#define MAX_SIZE 10000

using namespace std;


int main(void) {

    int N, target;

    cin >> N >> target;
       
    int* arr = new int[N];

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int i = 0, j = 0, sum = 0, cnt = 0;

    while (j <= N) {
        if (sum == target) {
            cnt++;
            sum -= arr[i++];
        }
        else if (sum < target) {
            sum += arr[j++];
        }
        else {
            sum -= arr[i++];
        }
    }

    cout << cnt << endl;

    delete[] arr;

    return 0;

   
}

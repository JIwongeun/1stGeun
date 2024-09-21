#include<iostream>
#include<algorithm>
#include<string>
#include<map>

using namespace std;


int main(void) {

    int result = 0;
    int N;
    
    cin >> N;

    map<string, int> bestseller;
    
    string book_name;

    for (int i = 0; i < N; i++) {
        cin >> book_name;
        bestseller[book_name]++;
    }
    
    for (auto str = bestseller.begin(); str != bestseller.end(); str++) {
        result = max(result, str->second);
    }

    for (auto str = bestseller.begin(); str != bestseller.end(); str++) {
        if (result == str->second) {
            cout << str->first;
            return 0;
        }
    }

    return 0;

   
}

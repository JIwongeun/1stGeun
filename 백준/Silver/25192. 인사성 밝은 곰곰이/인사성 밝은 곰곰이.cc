#include<iostream>
#include<set>
#include<string>

using namespace std;

int main(void) {
    set<string> s;  
    int N, ans = 0;
    cin >> N;
    string name;

    for (int i = 0; i < N; i++) {
        cin >> name;

        if (name == "ENTER") {
            s.clear(); 
        }
        else {
            if (s.find(name) == s.end()) {  
                s.insert(name);  
                ans++;  
            }
        }
    }

    cout << ans;

    return 0;
}

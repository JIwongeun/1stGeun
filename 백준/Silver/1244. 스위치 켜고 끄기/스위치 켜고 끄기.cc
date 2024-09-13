#include<iostream>
#include<vector>
#include<iterator>

using namespace std;


int main(void) {
    
    int num;
    cin >> num;

    vector<int> buttons(num);

    for (int i = 0; i < buttons.size(); i++) {
        cin >> buttons[i];
    }

    int sex, number, p;

    cin >> p;

    for (int i = 0; i < p; i++) {
        cin >> sex >> number;
        
        if (sex==1) {
            for (int j = number; j <= buttons.size(); j += number) {
                buttons[j - 1] = !buttons[j - 1];
            }
        }

        else {
            int left = number - 2, right = number;  
            buttons[number - 1] = !buttons[number - 1];  

            while (left >= 0 && right < buttons.size() && buttons[left] == buttons[right]) {
                buttons[left] = !buttons[left];
                buttons[right] = !buttons[right];
                left--;
                right++;
            }


        }
        
    }
    
    for (int i = 0; i < buttons.size(); i++) {
        cout << buttons[i];
        if ((i + 1) % 20 == 0) cout << '\n';
        else cout << " ";
     }
    return 0;
}

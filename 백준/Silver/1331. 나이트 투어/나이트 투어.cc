#include<iostream>
#include<string>
#define MAX 36

using namespace std;

int map[MAX][MAX];

int dx[8] = { -1,1,2,2,1,-1,-2,-2 };
int dy[8] = { 2,2,1,-1,-2,-2,-1,1 };

int night_tour(int x, int y, int nx_x, int nx_y) {

    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || ny < 0 || nx >= 6 || ny >= 6) {
            continue;
        }

        if (nx == nx_x && ny == nx_y) {
            if (map[nx][ny] == 0) {
                map[nx][ny]++;
                return 1;
            }

            else if (map[nx][ny] == 1) {
                return -1;
            }
        }
    }
    return -1;
}

int main(void) {
    int first_x = 0;
    int first_y = 0;


    int pre_x = 0;
    int pre_y = 0;
    int curx = 0;
    int cury = 0;
    string str;

    for (int i = 0; i < MAX; i++) {
        cin >> str;

        if (i == 0) {
            if (str[0] == 'A') {
                curx = 0;
            }
            else if (str[0] == 'B') {
                curx = 1;
            }
            else if (str[0] == 'C') {
                curx = 2;
            }
            else if (str[0] == 'D') {
                curx = 3;
            }
            else if (str[0] == 'E') {
                curx = 4;
            }
            else if (str[0] == 'F') {
                curx = 5;
            }
            cury = (str[1] - 48) - 1; 
            first_x = curx;
            first_y = cury;

        }
        else {
            
            pre_x = curx;
            pre_y = cury;

            if (str[0] == 'A') {
                curx = 0;
            }
            else if (str[0] == 'B') {
                curx = 1;
            }
            else if (str[0] == 'C') {
                curx = 2;
            }
            else if (str[0] == 'D') {
                curx = 3;
            }
            else if (str[0] == 'E') {
                curx = 4;
            }
            else if (str[0] == 'F') {
                curx = 5;
            }
            cury = (str[1] - 48) - 1;

            int N = night_tour(pre_x, pre_y, curx, cury);
            if (N == -1) {
                
                cout << "Invalid";
                return 0;
            }
            else {
                continue;
            }
        }
    }

   
    int N = night_tour(curx, cury, first_x, first_y);
    if (N == -1) {
        cout << "Invalid";
        return 0;
    }
    cout << "Valid";
    return 0;
}
#include<iostream>
#include<string>

using namespace std;

string king, stone;
int N;

int dx[8] = { 0,0,1,-1,-1,-1,1,1 };
int dy[8] = { 1,-1,0,0,1,-1,1,-1 };

int main(void) {
       
   
    string direction;
    cin >> king >> stone;
   
    int kx = '8' - king[1];
    int ky = king[0] - 'A';
    int sx = '8' - stone[1];
    int sy = stone[0] - 'A';


    cin >> N;

    int dir = 0;

    for (int i = 0; i < N; i++) {
        cin >> direction;

        if (direction == "R") dir = 0;
        else if (direction == "L") dir = 1;
        else if (direction == "B") dir = 2;
        else if (direction == "T") dir = 3;
        else if (direction == "RT") dir = 4;
        else if (direction == "LT") dir = 5;
        else if (direction == "RB") dir = 6;
        else if (direction == "LB") dir = 7;


        int kmx = kx + dx[dir];
        int kmy = ky + dy[dir];

        if (kmx < 0 || kmx >= 8 || kmy < 0 || kmy >= 8)
            continue;
        if (kmx == sx && kmy == sy)
        {
            int smx = sx + dx[dir];
            int smy = sy + dy[dir];
            if (smx < 0 || smx >= 8 || smy < 0 || smy >= 8) continue;
            sx = smx; sy = smy;
        }
        kx = kmx; ky = kmy;
    }
    
    cout << char(ky + 'A') << 8 - kx << endl;
    cout << char(sy + 'A') << 8 - sx << endl;
}
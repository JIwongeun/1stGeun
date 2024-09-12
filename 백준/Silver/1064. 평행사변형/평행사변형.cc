#include<iostream>
#include<cmath> 
#include<initializer_list>
#include<algorithm>

using namespace std;

typedef struct {
    double x;
    double y;
} Point;

double dist(double x1, double y1, double x2, double y2) {
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
}

bool is_collinear(Point A, Point B, Point C) {
    return (B.y - A.y) * (C.x - A.x) == (C.y - A.y) * (B.x - A.x);
}

int main(void) {
    Point A, B, C;

    
    cin >> A.x >> A.y >> B.x >> B.y >> C.x >> C.y;

    cout << fixed;
    cout.precision(15);
   
    if (is_collinear(A, B, C)) {
        cout << -1.0 << endl;
        return 0;
    }

  
    Point D1, D2, D3;

    D1.x = A.x + B.x - C.x;
    D1.y = A.y + B.y - C.y;

    D2.x = A.x + C.x - B.x;
    D2.y = A.y + C.y - B.y;

    D3.x = B.x + C.x - A.x;
    D3.y = B.y + C.y - A.y;

   
    double d1_distance = dist(A.x, A.y, D1.x, D1.y) + dist(B.x, B.y, D1.x, D1.y) + dist(B.x, B.y, C.x, C.y) + dist(C.x, C.y, A.x, A.y);
    double d2_distance = dist(A.x, A.y, B.x, B.y) + dist(B.x, B.y, C.x, C.y) + dist(C.x, C.y, D2.x, D2.y) + dist(D2.x, D2.y, A.x, A.y);
    double d3_distance = dist(A.x, A.y, B.x, B.y) + dist(B.x, B.y, D3.x, D3.y) + dist(C.x, C.y, D3.x, D3.y) + dist(C.x, C.y, A.x, A.y);

    cout << max({ d1_distance, d2_distance, d3_distance }) - min({ d1_distance, d2_distance, d3_distance }) << endl;

    return 0;
}

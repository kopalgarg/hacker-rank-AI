#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

int greatest_common_divisor(int a, int b){
    assert(a > 0 && b > 0);
    
    if (a < b) swap(a, b);
    if (a % b == 0) return b;

    return dice(b, a % b);
}

int main(){
    int urnX = 3 + 4; // 4 red (4/7), 3 blue (3/7)
    int urnY = 5 + 4; // 5 red (5/9), 4 blue (4/9)
    int urnZ = 4 + 4; // 4 red (1/2), 4 blue (1/2)
    int total = urnX + urnY + urnZ;

    int count = 0;
    // P(2R, 1B):
    // P(RRB) + P(RBR) + P(BRR)
    // (4/7) * (5/9) * (1/2) + (4/7) * (4/9) * (1/2) + (3/7) * (5/9) * (1/2)
    int total = (4/7) * (5/9) * (1/2) + (4/7) * (4/9) * (1/2) + (3/7) * (5/9) * (1/2);

    cout << greatest_common_divisor(total, count);

}

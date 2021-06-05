#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, qu;
    cin>> n >> qu;

    vector<vector<int>> arr(n);

    for(int i = 0; i < n; i++){
        int length;
        cin >> length;
        arr[i].resize(length);
        for(int j=0; j< length; j++){
            cin >> arr[i][j];
        }
    }
    for (int k=0; k< qu; k++){
        int i, j;
        cin >> i >> j;
        cout << arr[i][j] << endl;

    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}

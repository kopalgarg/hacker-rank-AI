#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

double median(const vector<int> &array) {

    double median = 0;
    int length = array.size();
    vector<int> copy(length);

    copy = array;
    sort (copy.begin(), copy.end());

    if( length % 2 != 0){
        median = (double) copy[(length-1)/2];
    } else{
        median = (double) (copy[(length/2)-1] + copy[length/2])/2;
    };
    return median;
}

int main() {
    int n;
    cin >> n;

    vector<int >arr(n);
    for(auto i = 0; i < n; i++){
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    int q1, q2, q3;

    q2 = median(arr);
    vector<int> l(arr.begin(), arr.begin()+n/2);
    vector<int> h;

    if (n %2 == 0){
        h.insert(h.end(), arr.begin()+n/2, arr.end());
    } else {
        h.insert(h.end(), arr.begin()+n/2+1, arr.end());
    }
    q1 = median(h);
    q3 = median(l);

    cout << q3 << "\n" << q2 << "\n" << q1;


    return 0;
}

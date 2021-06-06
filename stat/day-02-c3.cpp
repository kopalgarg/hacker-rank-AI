#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/* Standard Deviation */

double mean(const vector<int> &array) {

    double sum = 0;
    int length = array.size();
    for(int i = 0; i < length; i++){
        sum +=array[i];
    }
    double mean = sum / length;
    return mean;

}

int main(){

    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    int meanVal;

    meanVal = mean(arr);
    int sum = 0;

    for(int i = 0; i < n; i++){

        sum += (arr[i] - meanVal) * (arr[i] - meanVal);

    }
    double std = (double)sqrt(sum/n);

    printf("%.1f\n", std);
    return 0;

}

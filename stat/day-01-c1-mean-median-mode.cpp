#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

double mean(const vector<int> &array) {

    double sum = 0;
    int length = array.size();
    for(int i = 0; i < length; i++){
        sum +=array[i];
    }
    double mean = sum / length;
    return mean;

}

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

int mode(const vector<int> &array) {

    int mode = 0;
    int length = array.size();

    int max = 0;
    int count = 0;
    int current = 0;

    vector<int> copy(length);
    copy = array;
    sort (copy.begin(), copy.end());

    for(int i = 0; i < length; i++){

        if(copy[i]==current){
            count++;
        } else{
            count = 1;
            current = copy[i];
        }
        if (count > max){
            max = count;
            mode = copy[i];
        }
    }

    return mode;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> inArr(n);
    for(int i = 0; i < n; i++){
        cin >> inArr[i];
    }
    cout << mean(inArr) << endl;
    cout << median(inArr) << endl;
    cout << mode(inArr) << endl;
    return 0;
}

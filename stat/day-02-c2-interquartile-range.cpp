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

    vector<int >freq(n);
    int sum = 0;
    for(auto i = 0; i < n; i++){
        cin >> freq[i];
        sum += freq[i];
    }

    vector<int> arrS(sum);
    int index=0;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<freq[i]; j++)
        {
            arrS[index] = arr[i];
            index++;
        }
    }

    sort(arrS.begin(), arrS.end());

    int q1, q2, q3;

    q2 = median(arr);
    vector<int> l(arrS.begin(), arrS.begin()+sum/2);
    vector<int> h;

    if (sum %2 == 0){
        h.insert(h.end(), arrS.begin()+sum/2, arrS.end());
    } else {
        h.insert(h.end(), arrS.begin()+sum/2+1, arrS.end());
    }
    q1 = median(l);
    q3 = median(h);

    printf("%.1f", (q1-q3));
    return 0;
}

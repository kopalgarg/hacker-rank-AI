#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;
int ranking(vector<double> x, int i){
    
    vector<double> xSort;
    xSort = x;
    sort(xSort.begin(), xSort.end());
    vector<double>::iterator iter;
    iter = find(xSort.begin(), xSort.end(), x[i]);
    return distance(xSort.begin(), iter)+1;
}
int main() {
    
    int n; cin >> n;
    vector<double> x(n), y(n);
    for(int i = 0; i < n; i++){
        cin >> x[i];
    }    
    for(int i = 0; i < n; i++){
        cin >> y[i];
    }
    double diffRanking =0.00;
    for(int i = 0; i < n; i++){
        diffRanking += pow((ranking(x, i)-ranking(y, i)),2);
    }
    double coeff;
    coeff  = 1- (6*diffRanking)/(n*(pow(n,2)-1));
    printf("%0.3f", coeff);
    return 0;
}

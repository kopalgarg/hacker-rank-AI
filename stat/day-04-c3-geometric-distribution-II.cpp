#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    double p =  0.333; 
    double q = 1-p;
    int n = 5;
    double geometric_dist_probability;
    for(int i = 1; i<=5; i++){
        geometric_dist_probability+=pow(q, i-1)*p;
    }
    
    printf("%.3f", geometric_dist_probability);
    return 0;
}

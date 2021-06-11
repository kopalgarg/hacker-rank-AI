#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

double normalDist(double x, double avg, double stdev){
    double p = 0.5*(1 + erf((x-avg)/(stdev*sqrt(2.0))));
    return p;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int demand = 100;
    int avail = 250;
    double m = 2.4;
    double s = 2.0;
    
    double mean = demand * m;
    double std = sqrt(demand)*s;
        
    printf("%0.4f", normalDist(avail, mean, std));
    
    return 0;
}

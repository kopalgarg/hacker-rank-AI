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

    double m = 500;
    double s = 80;
    int num = 100;
    double z = 1.96;
    
    double moe = z * s/sqrt(num);

        
    printf("%0.2f\n%0.2f", m - moe, m + moe);

    return 0;
}

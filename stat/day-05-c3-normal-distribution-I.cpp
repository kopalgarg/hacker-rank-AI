#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

double cumulativeProbability(double x, double avg, double stdev){
    double p = 0.5*(1 + erf((x-avg)/(stdev*sqrt(2.0))));
    return p;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    double avg = 20;
    double stdev = 2;
    
    double aTime = 19.5;
    double bTimeL = 20;
    double bTimeU = 22;
    
    double sol1 = cumulativeProbability(aTime, avg, stdev);
    double sol2 = cumulativeProbability(bTimeU, avg, stdev) - cumulativeProbability(bTimeL, avg, stdev);
    
    printf("%0.3f\n%0.3f", sol1, sol2);
    
    return 0;
}

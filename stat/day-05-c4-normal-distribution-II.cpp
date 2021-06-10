#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

double cumulativeProbability(double x, double avg, double stdev){
    double p = 0.5*(1 + erf((x-avg)/(stdev*sqrt(2.0))));
    return p*100;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    double avg = 70;
    double stdev = 10;
    
    double sol1 = double(100)-cumulativeProbability(80, avg, stdev);
    double sol2 = double(100)-cumulativeProbability(60, avg, stdev);
    double sol3 = cumulativeProbability(60, avg, stdev);
    
    printf("%0.2f\n%0.2f\n%0.2f", sol1, sol2, sol3);
    
    return 0;
}

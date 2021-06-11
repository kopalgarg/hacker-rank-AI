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
    int max_weight = 9800;
    int num_box = 49;
    double mean_weight = 205;
    double std = 15;
    
    double mean = num_box * mean_weight;
    double stdev = sqrt(num_box) * std;
    
    printf("%0.4f", normalDist( max_weight, mean ,stdev));
    
    
    return 0;
}

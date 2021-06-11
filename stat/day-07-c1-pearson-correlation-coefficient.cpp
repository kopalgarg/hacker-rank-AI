#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

double pearsonCorrelationCoefficient(int n, double yStd, double xStd, double xMean, double yMean, double x[], double y[]){
    
    double numerator = 0;
    for (int i = 0; i < n; i++){
        
        numerator += ((xMean-x[i])*(yMean-y[i]));
        
    }
    
    double pcc=numerator/(n* xStd* yStd);
    
    return pcc;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    double x[n], y[n];
    double xSum = 0, ySum = 0;
    
    for (int i = 0; i < n; i++){
        cin >> x[i];
        xSum += x[i];
    }
    // compute mean x
    double xMean = (double) xSum/n;
    //compute sd x
    double xStdTemp = 0;
    for (int i = 0; i < n; i++){
        xStdTemp += pow(x[i]-xMean, 2);
    }
    double xStd = sqrt(xStdTemp/n);
    
    
    for (int i = 0; i < n; i++){
        cin >> y[i];
        ySum += y[i];
    }
    // compute mean y
    double yMean = (double) ySum/n;
    // compute sd y
    double yStdTemp = 0;
    for (int i = 0; i < n; i++){
        yStdTemp += pow(y[i]-yMean, 2);
    }
    double yStd = sqrt(yStdTemp/n);
    
    printf("%0.3f",pearsonCorrelationCoefficient(n, yStd, xStd, xMean, yMean, x, y));

    return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    double sumX=0;
    double sumY=0;
    double x[5], y[5];
    for(int i = 0; i < 5; i++){
        cin >> x[i];
        sumX += x[i];
        cin >> y[i];
        sumY += y[i];
    }
    
    double meanX = sumX / 5;
    double meanY = sumY / 5;
    
    double xiSq = 0.00;
    
    for(int i = 0; i < 5; i++){
        xiSq += pow(x[i],2);
    }
    
    double xiyiSum =0.00;
    
    for (int i = 0; i < 5; i++){
        
        xiyiSum += (x[i]*y[i]);
        
    }
    
    double b,a;
    
    b = ((5*xiyiSum)-(sumX*sumY))/((5 * xiSq) - pow(sumX,2));
    
    a = meanY - b*meanX;
    
    printf("%0.3f", a+b*80);
    
}

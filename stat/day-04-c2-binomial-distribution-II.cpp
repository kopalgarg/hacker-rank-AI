#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

double p = 0.12;
double q = 1-p;

// factorial as a recursive function:
int f(int n){
    if (n < 2){
        return (1);
    }
    else{
        return (n*f(n-1));
    }
}

// first part of the formula
double partA(int n, int r)
{
    return f(n)/(f(r)*f(n-r));
}

int main() {
    
    double sol1 = 0.00;
    double sol2 = 1.00;
    
    for (int i = 2; i >=0; i--){
        
        sol1 += partA(10, i) * pow(p, i) * pow(q, (10-i));
        
    }
    
    for (int i = 1; i >=0; i--){
        
        sol2 -= partA(10, i) * pow(p, i) * pow(q, (10-i));
        
    }
    printf("%0.3f\n", sol1);
    printf("%0.3f\n", sol2);
    return 0;
}

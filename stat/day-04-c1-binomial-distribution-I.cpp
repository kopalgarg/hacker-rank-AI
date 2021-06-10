#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


// factorial as a recursive function:
int factorial(int n){
    if (n < 2){
        return n;
    }
    else{
        return(n*factorial(n-1));
    }
}
// first part of the formula
double part_a(int n, int i)
{
    return factorial(n)/(factorial(i)*factorial(n-i));
}
int main() {
    double ratio_b;
    cin >> ratio_b;
    double ratio_g;
    cin >> ratio_g;
    
    double p = ratio_b / (ratio_b + ratio_g);
    double q = 1-p;
    
    double probability = 0.00;
    for (int i=6; i>=3; i--){
        probability += part_a(6, i)*pow(p, i)*pow(q, 6-i);   
    }
    printf("%0.3f\n", probability);
    
    return 0;
}


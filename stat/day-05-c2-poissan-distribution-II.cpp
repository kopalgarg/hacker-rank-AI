#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// factorial as a recursive function:
int factorial(int n){
    if (n < 2){
        return (1);
    }
    else{
        return (n*factorial(n-1));
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    double meanA = 0.88, meanB = 1.55;
    double cA = 160 + 40*(meanA + pow(meanA, 2));
    double cB = 128 + 40*(meanB + pow(meanB, 2));
    printf("%0.3f\n%0.3f", cA, cB);
    
    return 0;
}

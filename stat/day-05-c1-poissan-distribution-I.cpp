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
    double lambda = 2.5;
    int k = 5;  
    double e = 2.71;
    double prob = ((pow(lambda, k))*(pow(e, (-lambda))))/factorial(k);
    printf("%0.3f", prob);
    
    return 0;
}

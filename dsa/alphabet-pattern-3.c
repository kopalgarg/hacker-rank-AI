#include<stdio.h>
#include<math.h>
#include<limits.h>
#include<stdlib.h>

int main(){
    for (int i =1; i<=5; i++){

        for (int j=1; j<=i; j++){
            printf("%c", i+64);
        }
        printf("\n");
    }

    return(0);
}
/*
A
BB
CCC
DDDD
EEEEE
*/
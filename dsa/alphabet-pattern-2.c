#include<stdio.h>
#include<math.h>
#include<limits.h>
#include<stdlib.h>

int main(){
    for (int i =5; i>=1; i--){

        for (int j=1; j<=i; j++){
            printf("%c", j+64);
        }
        printf("\n");
    }

    return(0);
}
/*
ABCDE
ABCD
ABC
AB
A
*/
#include<stdio.h>
#include<math.h>
#include<limits.h>
#include<stdlib.h>

int main(){

    for (int i = 5; i >=1; i--){

        for (int j=i; j>=1; j--){

            printf("*");
        }
        printf("\n");
    }
    return(0);

}
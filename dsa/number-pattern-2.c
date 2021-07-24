#include<stdio.h>
#include<math.h>
#include<limits.h>
#include<stdlib.h>

int main(){

    int number =1;
    for (int i = 0; i < 5; i ++){

        for (int j = 0; j < i; j++){

            printf("%d", number);
            number ++;
        }
        printf("\n");
    }

    return(0);
}
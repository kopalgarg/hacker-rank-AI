#include<stdio.h>
#include<math.h>
#include<limits.h>
#include<stdlib.h>

int main(){

    for (int i = 1; i <= 10; i++){

            for (int k = 1; k <= 10-i; k++){
                printf(" ");
            }
            for (int j = 1; j <= 2*i-1; j++){
                printf("*");
            }

        printf("\n");
    }
    for (int i = 10; i >=1; i--){

            for (int k = 1; k <= 10-i; k++){
                printf(" ");
            }
            for (int j = 1; j <= 2*i-1; j++){
                printf("*");
            }

        printf("\n");
    }

    return(0);
}
/*
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
*/
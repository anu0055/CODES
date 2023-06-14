#include <stdio.h>
#include <stdlib.h>

int random(int a){
    int num= (rand() % (a+1));
    return num;
}
int function(int n){
    int i;
    if(n<=0){
        return 0;
    }
    else{
        i= random(n-1);
        printf("hello\n");
        return function(i) + function(n-1-i);
    }
}
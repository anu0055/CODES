#include <stdio.h>

int runningsum(int arr[], int size){
    int res[]={};
    res[0]= arr[0];
    for (int i = 1; i < size; i++)
    {
        res[i] = arr[i] + arr[i-1];
        printf("%d\n", res[i]);
    }
    return 0;
    
}

int main(){
int array[]= {1,2,34,5};
runningsum(array, 4);
return 0;
}
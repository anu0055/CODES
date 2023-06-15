#include <stdio.h>
int BinaryS(int arr[],int size, int element){
    int low, mid, high;
    low= 0;
    high = size-1;
  
    while(low<=high){
        mid = (low + high)/2;
        if(arr[mid] == element){
            return mid;
        }
        if(arr[mid] < element){
            low = mid+1;
        }
        else{
            high = mid-1;
        }
}
return -1;
}
int main(){
int arr[]= {1,2,3,40,500,650,888,981};
int size = sizeof(arr)/ sizeof(int);
int element = 500;
int search = BinaryS(arr, size, element);
printf("The index at which %d is %d", element, search);
return 0;
}
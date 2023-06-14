#include <stdio.h>

void display(int arr[], int n){
    for(int i=0; i<n; i++){
        printf("%d\n", arr[i]);
    }
}
int insert(int arr[], int element, int index, int size, int cap){
    if(size >= cap){
        return -1;
    }
    else{
        for (int i = (size-1); i >= index; i--){
            arr[i+1] = arr[i];
            
        }
    }
    arr[index] = element;
    size+=1;
        
}
    
int main(){
    
    int arr[100] = {1,2,3,4,10,28};
    display(arr, 6);
    printf("\n");
    insert(arr, 7, 4, 6, 100);
    display(arr, 7);
    return 0;

}


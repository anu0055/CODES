#include <stdio.h>

int main(){
int c;

c= getchar();

while (c!= EOF){  // this loop will run until there is an error or the file has ended.
 
    putchar(c);
    c= getchar();
}
return 0;
}
#include <stdio.h>

int main()
{
  int blank_char, tab_char, new_line;
  blank_char = 0;
  tab_char = 0;
  new_line = 0;
  int c;
  printf("Number of blanks, tabs, and newlines:\n");
  printf("Input few words/tab/newlines\n");
  for (; (c = getchar()) != EOF;)
  {
    if ( c == ' ' ){
      ++blank_char;
    }
    if ( c == '\t' ){
      ++tab_char;
    }
    if ( c == '\n' ){
      ++new_line;
    }
    
  }  
  printf("blank=%d,tab=%d,newline=%d\n",blank_char,tab_char,new_line); // to print the output press clt + z.
}

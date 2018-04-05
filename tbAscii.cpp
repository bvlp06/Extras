#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(void){
  	
	setlocale(LC_ALL, "Portuguese");
	int i;
  
	for(i = 0; i < 256; i++){
  	
	  printf("%d %c \t ", i, i);
	
	}
   
   return 0;
}

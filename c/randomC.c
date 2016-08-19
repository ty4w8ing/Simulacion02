#include <stdio.h>
#include <stdlib.h>  
#include <time.h>    

int main(int argc, char **argv) {
	long double random_number;
  	unsigned int seed = time(0);
  	unsigned int loop = 1000000;
  	FILE *out_file;
  	out_file = fopen("resultados/c.txt", "a");
	while(loop-- > 0){
		srand(seed++);
		random_number = ((long double) rand()/(RAND_MAX));	
		fprintf(out_file, "%.75LG\n", random_number);
	}
	fclose(out_file);
	return 0;
}
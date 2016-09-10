#include <stdio.h>
#include <stdlib.h>  
#include <time.h>    

int main(int argc, char **argv) {
	long double random_number;
	long double temp = 0;
  	unsigned int seed = time(0);
  	unsigned int loop = 1000000;
  	FILE *out_file;
  	out_file = fopen("resultados/c.txt", "w");
  	srand(seed);
	while(loop-- > 0){
		random_number = ((long double) rand()/(RAND_MAX));	
		if (temp != random_number){
			fprintf(out_file, "%.10LG\n", random_number);
			temp = random_number;
		}
		
	}
	fclose(out_file);
	return 0;
}
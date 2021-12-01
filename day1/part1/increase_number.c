#include <stdio.h>
#include <stdlib.h>
int main(){
	FILE *fnumbers = fopen("input.txt", "r");
	int previous_number, number;
	int counter = 0;
	char line[10];
	fgets(line, sizeof(line), fnumbers);	//ottengo il primo valore
	previous_number = (int)strtol(line, (char **)NULL, 10);	// lo converto in int
	while(fgets(line, sizeof(line), fnumbers)){		//scorro il file di testo riga per riga
		number = strtol(line, (char **)NULL, 10);
		if(number > previous_number){
			counter++;
		}
		previous_number = number;
	}
	printf("%d", counter);
}

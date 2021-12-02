#include <stdio.h>
#include <stdlib.h>
int main(){
	FILE *fnumbers = fopen("input.txt", "r");
	int elements = 2000;
	int temp_number;
	int numbers[elements];
	int counter = 0;
	char line[10];
	for(int i = 0; fgets(line, sizeof(line), fnumbers) != NULL; i++){
		temp_number = strtol(line, (char **)NULL, 10);
		numbers[i] = temp_number;
	}
	
	int window_index2 = 1;
	int window_sum1 = 0, window_sum2 = 0;
	for(int window_index1 = 0; window_index1 < elements - 3; window_index1++){
		window_sum1 = numbers[window_index1] + numbers[window_index1 + 1] + numbers[window_index1 + 2];
		window_sum2 = numbers[window_index2] + numbers[window_index2 + 1] + numbers[window_index2 + 2];
		if(window_sum2 > window_sum1){
			counter++;
		}
		window_index2++;
	}
	printf("%d", counter);

}

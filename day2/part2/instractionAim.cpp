#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	ifstream input_file;
	input_file.open("input.txt");
	int n_instructions = 1000;
	string instruction[n_instructions];

	for(int i = 0; i < n_instructions; i++){
		getline(input_file, instruction[i]);
	}

	int oriz_sum = 0, vert_sum = 0;
	int aim = 0;
	int value;	//index of the value in the input line
	int temp;	
	string temp_str;
	for(int i = 0; i < n_instructions; i++){
		value = instruction[i].length()-1;	//obtain the last index of the string that rappresent the value
		if(instruction[i][0] == 'f'){
			temp_str = instruction[i][value];
			temp = stoi(temp_str);
			oriz_sum += temp;
			vert_sum += aim * temp;
		}
		else if (instruction[i][0] == 'd'){
			temp_str = instruction[i][value];
			temp = stoi(temp_str);
			aim += temp;
		}
		else if (instruction[i][0] == 'u'){
			temp_str = instruction[i][value];
			temp = stoi(temp_str);
			aim -= temp;
		}

	}
	cout<<oriz_sum<<endl;
	cout<<vert_sum<<endl;
	cout<<(oriz_sum * vert_sum);
}
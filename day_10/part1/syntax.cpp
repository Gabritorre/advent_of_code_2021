#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <vector>
using namespace std;
#define LENGTH 106

int main(){
	ifstream input_file;
	input_file.open("input.txt");

	string instruction[LENGTH];
	for(int i = 0; i < LENGTH; i++){
		getline(input_file, instruction[i]);
	}
	stack<char> open_parentesis;
	stack<char> illegal;
	bool exitLine = true;
	for(int i = 0; i < LENGTH; i++){
		exitLine = true;
		for(int j = 0; j < instruction[i].length() && exitLine; j++){
			// if open braket I add to the stack the corresponding close bracket
			if(instruction[i][j] == '<'){
				open_parentesis.push('>');
			}
			else if(instruction[i][j] == '('){
				open_parentesis.push(')');
			}
			else if(instruction[i][j] == '['){
				open_parentesis.push(']');
			}
			else if (instruction[i][j] == '{'){
				open_parentesis.push('}');
			}
			else{	//if close bracket is equal to the last opened bracket
				if(instruction[i][j] == open_parentesis.top()){
					open_parentesis.pop();
				}
				else{	//syntax error
					illegal.push(instruction[i][j]);
					exitLine = false;
				}
			}
		}
		//reset stack
		while(!open_parentesis.empty()){
			open_parentesis.pop();
		}
	}

	int result = 0;
	while(!illegal.empty()) {
		char temp = illegal.top();
		if(temp == '>'){
			result += 25137;
		}
		else if(temp == ')'){
			result += 3;
		}
		else if(temp == ']'){
			result += 57;
		}
		else if (temp == '}'){
			result += 1197;
		}
		illegal.pop();
	}

	cout << result << endl;
}
using System;
using System.IO;
class lanternfish{
	static void Main(string[] args){
		string text = File.ReadAllText("input.txt");
		string[] temp_days = text.Split(',');
		long[] fish = new long[9];		// the index rappresent the days the content rapresent how many fish have index days remaining
		for(int i = 0; i < fish.Length; i++){
			fish[i] = 0;
		}
		
		for(int i = 0; i < fish.Length; i++){
			for(int j = 0; j < temp_days.Length; j++){
				if(i == Int32.Parse(temp_days[j])){
					fish[i]++;
				}
			}
		}
		long temp = 0;
		for(int i = 0; i < 256; i++){
			for(int j = 1; j < fish.Length; j++){
				if(j == 1){
					temp = fish[j];
				}
				else{
					fish[j-1] = fish[j];
				}
			}
			fish[6] += fish[0];		//day 6 can be reach in 2 ways: from 0 and from 7 so it's a sum
			fish[8] = fish[0];
			fish[0] = temp;
		}
		long result = 0;
		for(int i = 0; i < fish.Length; i++){
			result += fish[i];
		}
		Console.WriteLine(result);
	}
}
using System;
using System.Collections.Generic;
using System.IO;
class lanternfish{
	static void Main(string[] args){
		List<int> list = new List<int>();
		string text = File.ReadAllText("input.txt");
		string[] temp_days = text.Split(',');

		for(int i = 0; i < temp_days.Length; i++){
			list.Add(Int32.Parse(temp_days[i]));
		}
		int new_fish = 0;
		for(int i = 0; i < 80; i++){
			for(int j = 0; j < list.Count; j++){
				if(list[j] == 0){
					new_fish++;
					list[j] = 6;
				}
				else{
					list[j]--;
				}
			}

			for(int j = 0; j < new_fish; j++){
				list.Add(8);
			}
			new_fish = 0;
		}
		Console.WriteLine(list.Count);
	}
}
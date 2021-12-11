using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
class lanternfish{
	static void Main(string[] args){
		List<int> list = new List<int>();
		string text = File.ReadAllText("input.txt");
		string[] temp = text.Split(',');

		for(int i = 0; i < temp.Length; i++){
			list.Add(Int32.Parse(temp[i]));
		}

		int least_fuel = 99999999;
		for(int i = 0; i < list.Max(); i++) {
			int temp_fuel = 0;
			for(int j = 0; j < list.Count; j++) {
				int difference = Math.Abs(i - list[j]);
				temp_fuel += sumPrecedent(difference);
			}
			if(temp_fuel < least_fuel) {
				least_fuel = temp_fuel;
			}
		}
		Console.WriteLine(least_fuel);
	}

	public static int sumPrecedent(int number){
		if(number <= 0){
			return 0;
		}
		return number + sumPrecedent(number-1);
	}
}
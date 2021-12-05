
import java.io.FileNotFoundException;
import java.io.File;
import java.util.*;
public class diagnostic_co2_oxygen {
	public static void main(String[] args) {
		ArrayList<String> oxygen = new ArrayList<String>();
		ArrayList<String> co2;
		try {
			File inputFile = new File("input.txt");
			Scanner myReader = new Scanner(inputFile);
			while (myReader.hasNextLine()) {
				oxygen.add(myReader.nextLine());
			}
			myReader.close();
		} catch (FileNotFoundException e) {}

		co2 = new ArrayList<String>(oxygen);
		String oxygenValue = getValue(oxygen, 'o');
		String co2Value = getValue(co2, 'c');
		int oxygenDec = Integer.parseInt(oxygenValue, 2);
		int co2Dec = Integer.parseInt(co2Value, 2);
		System.out.println(oxygenDec * co2Dec);
	}

	public static String getValue(ArrayList<String> lines, char gas){	//gas = 'o' ->oxygen, gas = 'c' -> co2
		int true_counter = 0;
		int false_counter = 0;
		for (int i = 0; continueIteration(lines) && i < 12; i++) {
			for (String line : lines) {
				if(line.charAt(i) == '1'){
					true_counter++;
				}
				else if(line.charAt(i) == '0'){
					false_counter++;
				}
			}

			if (true_counter >= false_counter){		//1>=0 && oxygen -> remove line with 0 in that position | 1>=0 && co2 -> remove line with 1 in that position
				if(gas == 'o'){
					for (int j = 0; j < lines.size(); j++) {
						if(lines.get(j).charAt(i) == '0'){
							lines.set(j, "------------");
						}
					}
				}

				else if (gas == 'c'){
					for (int j = 0; j < lines.size(); j++) {
						if(lines.get(j).charAt(i) == '1'){
							lines.set(j, "------------");
						}
					}
				}
			}

			else{		//0>1 && oxygen-> remove line with 1 in that position | 0>1 && co2-> remove line with 0 in that position
				if(gas == 'o'){
					for (int j = 0; j < lines.size(); j++) {
						if(lines.get(j).charAt(i) == '1'){
							lines.set(j, "------------");
						}
					}
				}
				else if(gas == 'c'){
					for (int j = 0; j < lines.size(); j++) {
						if(lines.get(j).charAt(i) == '0'){
							lines.set(j, "------------");
						}
					}
				}
				
			}
			true_counter = 0;
			false_counter = 0;
		}

		String result = "";
		for(String line : lines){
			if(line != "------------"){
				result = line;
			}
		}
		return result;
	}

	//stop the iteration if there are not enough numbers available
	public static boolean continueIteration(ArrayList<String> lines){
		int numbers_left = 0; 
		for(String line : lines){
			if(line != "------------"){
				numbers_left++;
			}
		}
		if (numbers_left > 1){
			return true;
		}
		return false;
	}
}

import java.io.FileNotFoundException;
import java.io.File;
import java.util.*;
public class binary_diagnostic {
	public static void main(String[] args) {
		ArrayList<String> lines = new ArrayList<String>();
		try {
			File inputFile = new File("input.txt");
			Scanner myReader = new Scanner(inputFile);
			while (myReader.hasNextLine()) {
				lines.add(myReader.nextLine());
			}
			myReader.close();
		} catch (FileNotFoundException e) {}

		String gamma = "";
		String  epsilon = "";
		int trueCounter = 0;
		int falseCounter = 0;
		for (int i = 0; i < lines.get(0).length(); i++) {
			for (String line : lines) {
				if(line.charAt(i) == '1'){
					trueCounter++;
				}
				else{
					falseCounter++;
				}
			}
			if (trueCounter > falseCounter){
				gamma = gamma + "1";
			}
			else{
				gamma = gamma + "0";
			}
			trueCounter = 0;
			falseCounter = 0;
		}
		int gammaDec = Integer.parseInt(gamma, 2);
		epsilon = getEpsilon(gamma);
		int epsilonDec = Integer.parseInt(epsilon, 2);

		System.out.println(gammaDec * epsilonDec);
	}

	public static String getEpsilon(String gamma){
		String epsilon = "";
		for(int i = 0; i < gamma.length(); i++){
			if(gamma.charAt(i) == '1'){
				epsilon = epsilon + "0";
			}
			else{
				epsilon = epsilon + "1";
			}
		}
		return epsilon;
	}
}
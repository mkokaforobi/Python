import java.util.Scanner;

public class lowerCaseToUpperCase {
	public static void main(String[] args) {

        	Scanner input = new Scanner(System.in);

        	System.out.print("Enter a sentence in small letters: ");
        	String word = input.nextLine();

        	for (int number = 0; number < word.length(); number++) {
            	System.out.print(Character.toUpperCase(word.charAt(number)));
        	}
    	}
}
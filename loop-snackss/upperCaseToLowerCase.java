import java.util.Scanner;

public class upperCaseToLowerCase {
	public static void main(String[] args) {

        	Scanner input = new Scanner(System.in);

        	System.out.print("Enter a sentence in capital letters: ");
        	String word = input.nextLine();

        	for (int number = 0; number < word.length(); number++) {
            	System.out.print(Character.toLowerCase(word.charAt(number)));
        	}
    	}
}
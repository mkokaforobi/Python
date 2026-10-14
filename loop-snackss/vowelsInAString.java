import java.util.Scanner;

public class vowelsInAString {
	public static void main(String[] args) {

        	Scanner input = new Scanner(System.in);

        	System.out.print("Enter a sentence: ");
        	String word = input.nextLine();

        	int count = 0;

        	for (int number = 0; number < word.length(); number++) {

            		char letter = Character.toLowerCase(word.charAt(number));

            		if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u') {

                		count++;
            		}
        	}

        	System.out.println("Number of vowels = " + count);
    	}
}
import java.util.Scanner;

public class printCharacter {
	public static void main(String[] args) {

        	Scanner input = new Scanner(System.in);

        	System.out.print("Enter a phrase: ");
        	String word = input.nextLine();

        	for (int number = 0; number < word.length(); number++) {
           	System.out.println(word.charAt(number));
        	
		}
    

	}


}
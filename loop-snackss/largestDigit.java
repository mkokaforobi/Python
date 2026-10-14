import java.util.Scanner;

public class largestDigit {
	public static void main(String[] args) {

        	Scanner input = new Scanner(System.in);

        	System.out.print("Enter a number: ");
        	int number = input.nextInt();

        	int largest = 0;

        	while (number != 0) {

            	int digit = number % 10;

            	if (digit > largest) {
                largest = digit;
            	}

            	number = number / 10;
        	}

       		System.out.println("The largest digit is " + largest);
    
	}


}
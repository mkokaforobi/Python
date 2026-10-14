import java.util.Scanner;

public class printMultiplicationTable {
	
	public static void main(String[] args) {

        	Scanner input = new Scanner(System.in);

        	System.out.print("Enter a number: ");
        		
		int inputNumber = input.nextInt();

        	for (int number = 1; number <= 12; number++) {
            		System.out.println(inputNumber + " x " + number + " = " + (inputNumber * number));
        	}
    	

	}

}
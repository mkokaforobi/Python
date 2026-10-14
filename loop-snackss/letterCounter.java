import java.util.Scanner;

public class letterCounter {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String word = input.nextLine();

        int count = 0;

        for (int number = 0; number < word.length(); number++) {
            if (word.charAt(number) == 'e') {
                count++;
            }
        }

        System.out.println("The letter e appears " + count + " times.");
    }
}
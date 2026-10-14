public class countDivisibleBy7{

	public static void main(String[] args) {

		int count = 0;

		for (int number = 1; number <= 100; number++) {
    			if (number % 7 == 0) {
       			 count++;
    			}
		}

		System.out.println("Count = " + count);

	}

}


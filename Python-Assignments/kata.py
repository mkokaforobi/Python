class Kata:

 
       def isEven(integer):
        if integer % 2 == 0:
            return True
        else:
            return False


        def isPrimeNumber(integer):
        if integer < 2:
            return False

        for number in range(2, integer):
            if integer % number == 0:
                return False

        return True



      def subtract(integer1, integer2):
        if integer1 > integer2:
            return integer1 - integer2
        else:
            return integer2 - integer1



    def divide(integer1, integer2):
        if integer2 == 0:
            return 0

        return integer1 / integer2


    def factorOf(integer):
        count = 0

        for factor in range(1, integer + 1):
            if integer % factor == 0:
                count = count + 1

        return count


    def isSquare(integer):
        number = 0

        while number * number <= integer:
            if number * number == integer:
                return True

            number = number + 1

        return False



    def isPalindrome(integer):
        originalNumber = integer
        reversedNumber = 0

        while integer > 0:
            digit = integer % 10
            reversedNumber = reversedNumber * 10 + digit
            integer = integer // 10

        return originalNumber == reversedNumber



    def factorialOf(integer):
        factorial = 1

        for number in range(1, integer + 1):
            factorial = factorial * number

        return factorial




    def squareOf(integer):
        return integer * integer
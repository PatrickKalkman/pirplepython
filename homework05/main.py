"""
Python Is Easy course @Pirple.com
Homework Assignment #5: Basic Loops
Patrick Kalkman / patrick@simpletechture.nl

Details:

You're about to do an assignment called "Fizz Buzz", which is one of the
classic programming challenges. It is a favorite for interviewers, and a
shocking number of job-applicants can't get it right. But you won't be one of
those people. Here are the rules for the assignment
(as specified by Imran Gory):

Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the
multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

The one hint you'll likely need is:

There is a Python operator called "modulo", represented by the
percentage sign (%) that gives you the remainder left over after division.
So for example: 6 % 3 Equals zero. Because after dividing 6 by 3,
there is zero leftover. Whereas:

6 % 4 Equals 2. Because after dividing 6 by 4, there are 2
left over from the six. If that was confusing, don't worry. It will make more
sense as you use it. The point is: the modulo operator is useful for finding
out if X is a multiple of Y. If it is, then X % Y will yield zero.
Knowing this should help you complete this assignment without any issue.


Extra Credit:

Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print
statement: "prime". You should print this whenever you encounter a number
that is prime (divisible only by itself and one). As you implement this,
don't worry about the efficiency of the algorithm you use to check for primes.
It's okay for it to be slow.

"""


def isPrimeNumber(numberToCheck):

    if numberToCheck > 1:
        for number in range(2, numberToCheck):
            if numberToCheck % number == 0:
                return False

        return True
    else:
        return False


def performFizzBuzz():

    for number in range(1, 100):
        is_multiple_of_3 = (number % 3 == 0)
        is_multiple_of_5 = (number % 5 == 0)
        is_multiple_of_5_and_3 = is_multiple_of_3 and is_multiple_of_5
        is_prime_number = isPrimeNumber(number)

        if is_prime_number:
            print("prime")
        elif is_multiple_of_5_and_3:
            print("FizzBuzz")
        elif is_multiple_of_3:
            print("Fizz")
        elif is_multiple_of_5:
            print("Buzz")
        else:
            print(number)


performFizzBuzz()

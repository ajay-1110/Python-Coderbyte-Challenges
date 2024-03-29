"""/****************************************************************
 *                  CODERBYTE FIZZBUZZ CHALLENGE                *
 *                                                              *
 * Problem Statement                                            *
 * Have the function FizzBuzz(num) take the num parameter being *
 * passed and return all the numbers from 1 to num separated by *
 * spaces but replace every number that is divisible by 3       *
 * with the word "Fizz", replace every number that is divisible *
 * by 5 with the word "Buzz", & every number that is divisible  *
 * by both 3 and 5 with the word "FizzBuzz".                    *
 * For example: if num is 16, the code should return the string *
 * 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 *
 * The input will be within the range 1 - 50.                   *
 *                                                              *
 * Test Cases                                                   *
 * For example: if the input string is "Hello World and Coders" *
 * then your program should return the string                   *
 * sredoC dna dlroW olleH.                                      *
 *                                                              *
 * Examples                                                     *
 * Input 1: 3                                                   *
 * Output 1: "1 2 Fizz"                                         *
 *                                                              *
 * Input 2: 8                                                   *
 * Output 2: "1 2 Fizz 4 Buzz Fizz 7 8"                         *"""

def fizzbuzz(num):
    x = ''
    for i in range(1,num + 1):
        if i%3 == 0 and i%5 == 0:
            x += "FizzBuzz "
        elif i%3 == 0:
            x += 'Fizz '
        elif i%5 == 0:
            x += 'Buzz '
        else:
            x += str(i) + ' '
    return x.strip()

print(fizzbuzz(30))

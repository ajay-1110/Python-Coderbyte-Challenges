"""/****************************************************************
 *              CODERBYTE HAPPY NUMBERS CHALLENGE               *
 *                                                              *
 * Problem Statement                                            *
 * Have the function HappyNumbers(num) determine if a number is *
 * Happy, which is a number whose sum of the square of the      *
 * digits eventually converges to 1. Return true if it's a Happy*
 * number, otherwise return false.                              *
 *                                                              *
 * For example: the number 10 is Happy because 1^2 + 0^2        *
 * converges to 1.                                              *
 *                                                              *
 * Examples                                                     *
 * Input 1: 1                                                   *
 * Output 1: true                                               *
 *                                                              *
 * Input 2: 101                                                 *
 * Output 2: false                                              *
 *                                                              *
 ***************************************************************/"""

def is_happy_number(n):
    s = set()
    while n != 1 and n not in s:
        s.add(n)
        n = sum(int(i)**2 for i in str(n))
    return n == 1

print(is_happy_number(101))

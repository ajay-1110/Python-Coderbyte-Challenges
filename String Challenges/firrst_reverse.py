"""/****************************************************************
 *             CODERBYTE FIRST REVERSE CHALLENGE                *
 *                                                              *
 * Problem Statement                                            *
 * Have the function FirstReverse(str) take the str parameter   *
 * being passed and return the string in reversed order.        *
 *                                                              *
 * Test Cases                                                   *
 * For example: if the input string is "Hello World and Coders" *
 * then your program should return the string                   *
 * sredoC dna dlroW olleH.                                      *
 *                                                              *
 * Examples                                                     *
 * Input 1: coderbyte                                           *
 * Output 1: etybredoc                                          *
 *                                                              *
 * Input 2: I Love Code                                         *
 * Output 2: edoC evoL I                                        *
 *                                                              *"""

def firstreverse(str):
    return str[::-1]

print(firstreverse("I Love Code"))

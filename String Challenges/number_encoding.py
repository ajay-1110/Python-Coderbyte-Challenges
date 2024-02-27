"""
 ****************************************************************
 *           CODERBYTE NUMBER ENCODING CHALLENGE                *
 *                                                              *
 * Problem Statement                                            *
 * Have the function NumberEncoding(str) take the str parameter *
 * and encode the message according to the following rule:      *
 * encode every letter into its corresponding numbered position *
 * in the alphabet. Symbols and spaces will also be used in the *
 * input. For example: if str is "af5c a#!" then your program   *
 * should return 1653 1#!.                                      *
 *                                                              *
 * Examples                                                     *
 * Input 1: "hello 45"                                          *
 * Output 1: 85121215 45                                        *
 *                                                              *
 * Input 2: "jaj-a"                                             *
 * Output 2: 10110-1                                            *"""

def numberencoding(strn):
    letter = "abcdefghijklmnopqrstuvwxyz"
    new = ""
    for i in strn.lower():
        if i in letter:
            a = letter.index(i) + 1
            new += str(a)
        else:
            new += i
    return new

print(numberencoding("jaj-a"))

"""/****************************************************************
 *             CODERBYTE NUMBER REVERSE CHALLENGE               *
 *                                                              *
 * Problem Statement                                            *
 * Have the function NumberReverse(str) take the str parameter	*
 * being passed which will be a string of numbers, and return a *
 * new string with the numbers in reverse order.  		*
 *                                                              *
 * Examples                                                     *
 * Input 1: "1 2 3"                                             *
 * Output 1: 3 2 1                                              *
 *                                                              *
 * Input 2: "10 20 50"                                          *
 * Output 2: 50 20 10                                           *"""


import re
def numberreverse(str):
    x = re.sub(r'[^0-9 ]',"",str).split(" ")
    y = ""
    z = x[::-1]
    for i in z:
        y = y + i + ' '
    return y

print(numberreverse("10 20 50"))

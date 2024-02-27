"""/****************************************************************
 *                  CODERBYTE PLUS MINUS CHALLENGE              *
 *                                                              *
 * Problem Statement                                            *
 * Have the function PlusMinus(num) read the num parameter being*
 * passed which will be a combination of 1 or more single       *
 * digits, and determine if it's possible to separate the digits*
 * with either a plus or minus sign to get the final expression *
 * to equal zero.                                               *
 *                                                              *
 * For example: if num is 35132 then it's possible to separate  *
 * the digits the following way, 3 - 5 + 1 + 3 - 2, and this    *
 * expression equals zero.                                      *
 *                                                              *
 * Your program should return a string of the signs you used, so*
 * for this example your program should return -++-. If it's not* 
 * possible to get the digit expression to equal zero, return   *
 * the string not possible.                                     *
 *                                                              *
 * If there are multiple ways to get the final expression to    *
 * equal zero, choose the one that contains more minus          *
 * characters. For example: if num is 26712 your program        *
 * should return -+-- and not +-+-.                             *
 *                                                              *
 * Examples                                                     *
 * Input 1: 199                                                 *
 * Output 1: not possible                                       *
 *                                                              *
 * Input 2: 26712                                               *
 * Output 2: -+--                                               *
 *                                                              *
 ***************************************************************/"""

def plusminus(num):
    a = str(num)
    n = len(a)
    for i in range(1<<(n-1)):
        expression = a[0]
        for j in range(n-1):
            if (i>>j) & 1:
                expression += '+' + a[j+1]
            else:
                expression += '-' + a[j+1]
        if eval(expression) == 0:
            return "".join(i for i in expression if i in "+-")
    return "not possible"
        
print(plusminus(26712))

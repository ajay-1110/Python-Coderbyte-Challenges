"""/****************************************************************
 *              CODERBYTE SIMPLE EVENS CHALLENGE                *
 *                                                              *
 * Problem Statement                                            *
 * Have the function SimpleEvens(num) check whether every single*
 * number in the passed in parameter is even. If so, return the * 
 * string true, otherwise return the string false. For example: *
 * if num is 4602225 your program should return the string      *
 * false because 5 is not an even number.                       *
 *                                                              *
 * Examples                                                     *
 * Input 1: 2222220222 		                                *
 * Output 1: true                                               *
 *                                                              *
 * Input 2: 20864646452                                         *
 * Output 2: false                                              *
 *                                                              *
 ***************************************************************/"""

def simpleeven(num):
    for i in str(num):
        if int(i)%2 != 0:
            return False
    return True

print(simpleeven(4602225))

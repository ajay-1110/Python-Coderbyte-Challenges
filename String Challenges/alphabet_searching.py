"""
 *             CODERBYTE ALPHABET SEARCHING CHALLENGE           *
 *                                                              *
 * Problem Statement                                            *
 * Have the function AlphabetSearching(str) take the string     *
 * parameter being passed and return the string true if every   *
 * single letter of the English alphabet exists in the string,  *
 * otherwise return the string false.                           *
 * For example: if str is "zacxyjbbkfgtbhdaielqrm45pnsowtuv"    *
 * then your program should return the string true because every*
 * character in the alphabet exists in this string even though  *
 * some characters appear more than once.                       *
 *                                                              *
 * Examples                                                     *
 * Input 1: abcdefghijklmnopqrstuvwxyyyy                        *
 * Output 1: false                                              *
 *                                                              *
 * Input 2: abc123456kmo                                        *
 * Output 2: false 
"""

#First Solution - 
def alpha(strn):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    for i in letters:
        if i not in strn.lower():
            return False
    return True

print(alpha("qwertyuopasdfdjdjghjklzxcvbnm"))

#Second Solution (using regex) - 
import re
def alpha2(strn):
    b = set(re.sub(r'[^a-zA-Z]','',strn).lower())
    if len(b) == 26:
        return True
    else:
        return False

print(alpha2("qwertyuiokdkdkpasdfghjklzxcvbnm"))

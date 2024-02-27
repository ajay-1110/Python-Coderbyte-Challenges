"""
 *             CODERBYTE ALPHABET SOUP CHALLENGE                *
 *                                                              *
 * Problem Statement                                            *
 * Have the function AlphabetSoup(str) take the str string      *
 * parameter being passed and return the string with the        *
 * letters in alphabetical order (ie. hello becomes ehllo).     *
 * Assume numbers and punctuation symbols will not be included  *
 * in the string.                                               *
 *                                                              *
 * Examples                                                     *
 * Input 1: coderbyte                                           *
 * Output 1: bcdeeorty  
"""

def sort(strn):
    x = strn.split(' ')
    y = ''
    for i in x:
        y+= ''.join(j for j in sorted(i)) + ' '
    return y

print(sort('coderbyte'))

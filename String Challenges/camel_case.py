"""
/****************************************************************
 *             CODERBYTE CAMEL CASE CHALLENGE                   *
 *                                                              *
 * Problem Statement                                            *
 * Have the function CamelCase(str) take the str parameter being*
 * passed and return it in proper camel case format where the   *
 * first letter of each word is capitalized (excluding the first*
 * letter). The string will only contain letters and some       *
 * combination of delimiter punctuation characters separating   *
 * each word.                                                   *
 *                                                              *
 * For example: if str is "BOB loves-coding" then your program  *
 *  should return the string bobLovesCoding.                    *
 *                                                              *
 * Examples                                                     *
 * Input 1: "cats AND*Dogs-are Awesome"                         *
 * Output 1: catsAndDogsAreAwesome                              *
 *                                                              *
 * Input 2: "a b c d-e-f%g"                                     *
 * Output 2: aBCDEFG                                            *
"""

import re
def camelcase(strn):
    x = strn.title()
    y = re.sub(r'[^a-zA-Z0-9]',' ',x).split(' ')
    z = '' + ''.join(y[0].lower())
    for i in range(1,len(y)):
        z += y[i]
    
    return z

print(camelcase('cats AND*Dogs-are Awesome'))

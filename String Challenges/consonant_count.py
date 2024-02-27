"""
/****************************************************************
 *             CODERBYTE CONSONANT COUNT CHALLENGE              *
 *                                                              *
 * Problem Statement                                            *
 * Have the function ConsonantCount(str) take the str string	*
 * parameter being passed and return the number of consonants 	*
 * the string contains.  					*
 *                                                              *
 * Examples                                                     *
 * Input 1: "Hello World"                                       *
 * Output 1: 7		                                        *
 *                                                              *
 * Input 2: "Alphabets"                                         *
 * Output 2: 6                                                  *
"""

#First solution -
def consonant_count(strn):
    letters = 'bcdfghjklmnpqrstvwxyz'
    count = 0
    for i in strn.lower():
        if i in letters:
            count += 1
    return count
print(consonant_count("Hello World"))

#Second solution -
import re
def consonant(strn):
    x = re.sub(r'[^a-zA-Z]',"",strn).lower()
    count = 0
    v = 'aeiou'
    for i in x:
        if i not in v:
            count += 1
    return count
print(consonant('Hello World'))

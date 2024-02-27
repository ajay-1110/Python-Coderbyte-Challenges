"""/****************************************************************
 *             CODERBYTE DIFFERENT CASES CHALLENGE              *
 *                                                              *
 * Problem Statement                                            *
 * Have the function DifferentCases(str) take the str parameter *
 * being passed and return it in upper camel case format where  *
 * the first letter of each word is capitalized. The string will*
 * only contain letters and some combination of delimiter       *
 * punctuation characters separating each word.                 *
 *                                                              *
 * Examples                                                     *
 * Input 1: "Daniel LikeS-coding"                               *
 * Output 1: DanielLikesCoding                                  *
 *                                                              *
 * Input 2: "cats AND*Dogs-are Awesome"                         *
 * Output 2: CatsAndDogsAreAwesome                              *
 *                                                              *
 * Input 3: "a b c d-e-f%g"                                     *
 * Output 3: ABCDEFG                                            *"""

import re
def differentcase(str):
    a = str.title()
    x = re.sub(r'[^a-zA-Z0-9]',' ',a).split(' ')
    new = ''
    for i in x:
        new += i
    return new

print(differentcase('cats AND*Dogs-are Awesome'))

"""/****************************************************************
 *             CODERBYTE VOWEL COUNT CHALLENGE                  *
 *                                                              *
 * Problem Statement                                            *
 * Have the function VowelCount(str) take the str string        *
 * parameter being passed and return the number of vowels the   *
 * string contains (ie. "All cows eat grass and moo" would      *
 * return 8). Do not count y as a vowel for this challenge.     *
 *                                                              *
 * Examples                                                     *
 * Input 1: "hello"                                             *
 * Output 1: 2                                                  *
 *                                                              *
 * Input 2: "coderbyte"                                         *
 * Output 2: 3                                                  *"""

def vowelcount(strn):
    count = 0
    for i in strn:
        if i in "aeiouAEIOU":
            count += 1
    return count

print(vowelcount("hello"))

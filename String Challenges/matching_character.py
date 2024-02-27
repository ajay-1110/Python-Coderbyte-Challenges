""" *           CODERBYTE MATCHING CHARACTERS CHALLENGE            *
 *                                                              *
 * Problem Statement                                            *
 * Have the function MatchingCharacters(str) take the str       *
 * parameter being passed and determine the largest number of   *
 * unique characters that exists between a pair of matching     *
 * letters anywhere in the string.                              *
 *                                                              *
 * For example: if str is "ahyjakh" then there are only two     *
 * pairs of matching letters, the two a's and the two h's.      *
 * Between the pair of a's there are 3 unique characters:       *
 * h, y, and j.                                                 *
 * Between the h's there are 4 unique characters: y, j, a, & k. *
 * So for this example your program should return 4.            *
 *                                                              *
 * Another example: if str is "ghececgkaem" then your program   *
 * should return 5 because the most unique characters exists    *
 * within the farthest pair of e characters. The input string   *
 * may not contain any character pairs, and in that case your   *
 * program should just return 0. The input will only consist of *
 * lowercase alphabetic characters.                             *
 *                                                              *
 * Examples                                                     *
 * Input 1: "mmmerme"                                           *
 * Output 1: "3"                                                *
 *                                                              *
 * Input 2: "abccdefghi"                                        *
 * Output 2: "0"                                                *"""

def matchingcharacter(str):
    largest_count = 0
    for i in range(len(str)-1):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                stringbetween = str[i+1:j]
                length = len(set(stringbetween))
                if length > largest_count:
                    largest_count = length
    return largest_count

print(matchingcharacter("ahyjakh"))

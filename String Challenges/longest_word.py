"""/****************************************************************
 *           CODERBYTE LONGEST WORD CHALLENGE                   *
 *                                                              *
 * Problem Statement                                            *
 * Have the function LongestWord(sen) take the sen parameter    *
 * being passed and return the largest word in the string.      *
 * If there are two or more words that are the same length,     *
 * return the first word from the string with that length.      *
 * Ignore punctuation and assume sen will not be empty.         *
 *                                                              *
 * Examples                                                     *
 * Input 1: "fun&!! time"                                       *
 * Output 1: time                                               *
 *                                                              *
 * Input 2: "I love dogs"                                       *
 * Output 2: love                                               *"""
import re
def longestword(str):
    new = re.sub(r"[^a-zA-Z0-9 ]","",str).split(" ")
    longest = new[0]
    for i in range(1,len(new)):
        if len(new[i]) > len(longest):
            longest = new[i]
    return longest

print(longestword("I love dogs"))

import re
def longestword1(str):
    new = re.sub(r"[^a-zA-Z0-9 ]","",str).split(" ")
    new.sort(key=len,reverse=True)
    return new[0]

print(longestword1("I love dogs"))

"""/****************************************************************
 *             CODERBYTE WORD COUNT CHALLENGE                   *
 *                                                              *
 * Problem Statement                                            *
 * Have the function WordCount(str) take the str string         *
 * parameter being passed and return the number of words the    *
 * string contains (e.g. "Never eat shredded wheat or cake"     *
 * would return 6). Words will be separated by single spaces.   *
 *                                                              *
 * Examples                                                     *
 * Input 1: "Hello World"                                       *
 * Output 1: 2                                                  *
 *                                                              *
 * Input 2: "one 22 three"                                      *
 * Output 2: 3                                                  *"""

def wordcount(strn):
    x = strn.split(" ")
    return len(x)

print(wordcount("Never eat shredded wheat or cake"))

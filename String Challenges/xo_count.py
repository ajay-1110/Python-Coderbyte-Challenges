"""/****************************************************************
 *             CODERBYTE EX OH CHALLENGE                        *
 *                                                              *
 * Problem Statement                                            *
 * Have the function ExOh(str) take the str parameter being     *
 * passed & return the string true if there is an equal number  *
 * of x's & o's, otherwise return the string false. Only these  *
 * two letters will be entered in the string, no punctuation or *
 * numbers. For example: if str is "xooxxxxooxo" then the       *
 * output should return false because there are 6 x's and 5 o's *
 *                                                              *
 * Examples                                                     *
 * Input 1: xooxxo                                              *
 * Output 1: true                                               *
 *                                                              *
 * Input 2: x                                                   *
 * Output 2: false                                              *"""

def xo(str):
    xcount = 0
    ycount = 0
    for i in str.lower():
        if i == 'x':
            xcount += 1
        elif i == 'o':
            ycount += 1
        else:
            pass
    if xcount == ycount:
        return True
    return False

print(xo("Xoox"))

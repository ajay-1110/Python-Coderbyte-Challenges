"""/****************************************************************
 *               CODERBYTE EVEN PAIRS CHALLENGE		        *
 *                                                              *
 * Problem Statement                                            *
 * Have the function EvenPairs(str) take the str parameter being*
 * passed & determine if a pair of adjacent even numbers exists *
 * anywhere in the string. If a pair exists, return the string  *
 * true, otherwise return false. For example: if str is         *
 * "f178svg3k19k46" then there are two even numbers at the end  *
 * of the string, "46" so your program should return the string *
 * true. Another example: if str is "7r5gg812" then the pair is *
 * "812" (8 & 12) so your program should return the string true *
 *                                                              *
 * Examples                                                     *
 * Input 1: "3gy41d216"                                         *
 * Output 1: true                                               *
 *                                                              *
 * Input 2: "f09r27i8e67"                                       *
 * Output 2: false                                              *
 *                                                              *
 ***************************************************************/"""

from itertools import combinations
def evenpairs(strn):
    new = ""
    for i in strn:
        if i not in "1234567890":
            new += ' '
        else:
            new += i
    x = new.strip().split()
    for i in x:
        if len(i) == 1 or len(i) == 0:
            pass
        elif len(i) == 2:
            if int(i[0]) % 2 == 0 and int(i[1]) % 2 == 0:
                return True
        else:
            result = []
            for j in range(1, len(i)):
                result.extend(combinations([i[:j], i[j:]], 2))
            for pair in result:
                if int(pair[0]) % 2 == 0 and int(pair[1]) % 2 == 0:
                    return True
    return False

print(evenpairs("3gy41d216"))

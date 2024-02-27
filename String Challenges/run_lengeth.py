"""/****************************************************************
 *              CODERBYTE RUN LENGTH CHALLENGE                  *
 *                                                              *
 * Problem Statement                                            *
 * Have the function RunLength(str) take the str parameter being*
 * passed and return a compressed version of the string using   *
 * the Run-length encoding algorithm. This algorithm works by   *
 * taking the occurrence of each repeating character and        *
 * outputting that number along with a single character of the  *
 * repeating sequence.                                          *
 * For example: "wwwggopp" would return 3w2g1o2p.               *
 * The string will not contain any numbers, punctuation,        *
 * or symbols.                                                  *
 *                                                              *
 * Examples                                                     *
 * Input 1: "aabbcde"                                           *
 * Output 1: 2a2b1c1d1e                                         *
 *                                                              *
 * Input 2: "wwwbbbw"                                           *
 * Output 2: 3w3b1w                                             *"""

def runlength(strn):
    compressed = ""
    count = 1
    
    for i in range(len(strn)):
        if i == len(strn) - 1 or strn[i] != strn[i + 1]:
            compressed += str(count) + strn[i]
            count = 1
        else:
            count += 1
    
    return compressed

print(runlength("wwwbbhh"))

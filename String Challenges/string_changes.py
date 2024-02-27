"""/****************************************************************
 *             CODERBYTE STRING CHANGES CHALLENGE               *
 *                                                              *
 * Problem Statement                                            *
 * Have the function StringChanges(str) take the str parameter  *
 * being passed, which will be a string containing letters from *
 * the alphabet, and return a new string based on the following *
 * rules. Whenever a capital M is encountered, duplicate the    *
 * previous character (then remove the M), and whenever a       *
 * capital N is encountered remove the next character from the  *
 * string (then remove the N). All other characters in the      *
 * string will be lowercase letters.                            *
 * For example: "abcNdgM" should return "abcgg".                *
 * The final string will never be empty.                        *  
 *                                                              *
 * Examples                                                     *
 * Input 1: "MrtyNNgMM"                                         *
 * Output 1: rtyggg                                             *
 *                                                              *
 * Input 2: "oMoMkkNrrN"                                        *
 * Output 2: ooookkr                                            *"""

def stringchanges(strn):
    result = []
    i = 0
    while i < len(strn):
        if strn[i] == 'M':
            if len(result) > 0:
                result.append(result[-1])
            i += 1
        elif strn[i] == 'N':
            i+= 2
        else:
            result.append(strn[i])
            i += 1
    return ''.join(result)

print(stringchanges("MrtyNNgMM"))

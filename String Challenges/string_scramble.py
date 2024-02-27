"""/****************************************************************
 *             CODERBYTE STRING SCRAMBLE CHALLENGE              *
 *                                                              *
 * Problem Statement                                            *
 * Have the function StringScramble(str1,str2) take both        * 
 * parameters being passed and return the string true if a      *
 * portion of str1 characters can be rearranged to match str2,  *
 * otherwise return the string false.                           *
 * For example: if str1 is "rkqodlw" and str2 is "world" the    *
 * output should return true. Punctuation and symbols will not  *
 * be entered with the parameters.                              *
 *                                                              *
 * Examples                                                     *
 * Input 1: "cdore" & "coder"                                   *
 * Output 1: true                                               *
 *                                                              *
 * Input 2: "h3llko" & "hello"                                  *
 * Output 2: false                                              *"""

#First solution - 
def stringscramble(str1,str2):
    raw_str = str1
    match_str = str2
    for i in match_str:
        if i not in raw_str:
            return False
        updated_str = raw_str.replace(i,'',1)
        updated_str = raw_str
    return True

print(stringscramble("h3llko" , "hello"))

#Second solution - 
def strscram(str1,str2):
    x = "".join(sorted(str1))
    y = "".join(sorted(str2))
    if y in x:
        return True
    return False

print(strscram("h3llko" , "hello"))

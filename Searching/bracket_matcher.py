"""/****************************************************************
 *          CODERBYTE BRACKET MATCHER CHALLENGE		        *
 *                                                              *
 * Problem Statement                                            *
 * Have the function BracketMatcher(str) take the str parameter	*
 * being passed and return 1 if the brackets are correctly	*
 * matched and each one is accounted for. Otherwise return 0.	*
 * For example: if str is "(hello (world))", then the output	*
 * should be 1, but if str is "((hello (world))" the the output	*
 * should be 0 because the brackets do not correctly match up.	*
 * Only "(" and ")" will be used as brackets. If str contains	*
 * no brackets return 1.    					*
 *                                                              *
 * Examples                                                     *
 * Input 1: "(coder)(byte))"                                    *
 * Output 1: 0                                                  *
 *                                                              *
 * Input 2: "(c(oder)) b(yte)"                                  *
 * Output 2: 1                                                  *
 *                                                              *
 ***************************************************************/"""

def BracketMatcher(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
    return 1 if count == 0 else 0

print(BracketMatcher("((hello (world))" ))

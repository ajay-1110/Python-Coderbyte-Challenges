"""/****************************************************************
 *             CODERBYTE FORMATTED NUMBERS CHALLENGE            *
 *                                                              *
 * Problem Statement                                            *
 * Have the function FormattedNumber(strArr) take the strArr    *
 * parameter being passed, which will only contain a single     *
 * element, and return the string true if it is a valid number  *
 * that contains only digits with properly placed decimals &    *
 * commas, otherwise return the string false.                   *
 * For example: if strArr is ["1,093,222.04"] then your program *
 * should return the string true, but if the input were         *
 * ["1,093,22.04"] then your program should return the string   *
 * false. The input may contain characters other than digits.   *
 *                                                              *
 * Examples                                                     *
 * Input 1: ["0.232567"]                                        *
 * Output 1: true                                               *
 *                                                              *
 * Input 2: ["2,567.00.2"]                                      *
 * Output 2: false                                              *
 *                                                              *"""

from collections import Counter
import re
def formatednumber(strArr):
    l = []
    for i in strArr:
            c = Counter(i)
            if c['.'] > 1:
                l.append('false')
            else:
                x = i.split('.')
                y = x[0]
                removequoma = re.sub(r'[^0-9]',"",y)
                rev_y = removequoma[::-1]
                correct_strn = ''
                for k,char in enumerate(rev_y):
                    if (k+1)%3 ==0:
                        correct_strn += char
                        correct_strn += ','
                    else:
                        correct_strn += char
                if correct_strn[::-1] == y:
                    l.append('true')
                else:
                    l.append('false')
    for i in l:
        if i == 'false':
            return False
    return True

print(formatednumber(["0.232567", "0.23.2567"]))

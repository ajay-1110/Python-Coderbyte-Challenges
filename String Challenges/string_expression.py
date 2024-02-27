"""/****************************************************************
 *             CODERBYTE STRING EXPRESSION CHALLENGE            *
 *                                                              *
 * Problem Statement                                            *
 * Have the function StringExpression(str) read the str         *
 * parameter being passed which will contain the written out    *
 * version of the numbers 0-9 and the words "minus" or "plus" & *
 * convert the expression into an actual final number written   *
 * out as well.                                                 *
 * For example: if str is "foursixminustwotwoplusonezero" then  *
 * this converts to "46 - 22 + 10" which evaluates to 34 and    *
 * your program should return the final string threefour.       *
 * If your final answer is negative it should include the       *
 * word "negative."                                             *
 *                                                              *
 * Examples                                                     *
 * Input 1: "onezeropluseight"                                  *
 * Output 1: oneeight                                           *
 *                                                              *
 * Input 2: oneminusoneone                                      *
 * Output 2: negativeonezero                                    *"""

def stringexpression(strn):
    numbers = {'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'minus': '-',
        'plus' : '+'}
    wordsToNumber = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    for word,num in numbers.items():
        strn = strn.replace(word,num)
    result = eval(strn)
    res = str(result)
    if result<0:
        res += 'negative' + res[1:]
    r = ""
    for i in res:
        r += wordsToNumber[i]
    return r

print(stringexpression("onezeropluseight"))

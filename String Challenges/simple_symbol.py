"""/****************************************************************
 *             CODERBYTE SIMPLE SYMBOLS CHALLENGE               *
 *                                                              *
 * Problem Statement                                            *
 * Have the function SimpleSymbols(str) take the str parameter  *
 * being passed and determine if it is an acceptable sequence   *
 * by either returning the string true or false. The str        *
 * parameter will be composed of + and = symbols with several   *
 * characters between them (ie. ++d+===+c++==a) and for the     *
 * string to be true each letter must be surrounded by          *
 * a + symbol. So the string to the left would be false.        *
 * The string will not be empty & will have at least one letter *
 *                                                              *
 * Examples                                                     *
 * Input 1: "+d+=3=+s+"                                         *
 * Output 1: true                                               *
 *                                                              *
 * Input 2: "f++d+"                                             *
 * Output 2: false                                              *"""

def simplesymbols(strn):
    if strn[0].isalpha() or strn[-1].isalpha():
            return 'false'
    for i in range(1,len(strn)-1):
        if strn[i].isalpha():
            if strn[i+1] != '+' or strn[i-1] != '+':
                return 'false'
    return 'true'
    
print(simplesymbols("+d+=3=+s+"))
            

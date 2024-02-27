"""/****************************************************************
 *          CODERBYTE SECOND GREATEST LOWEST CHALLENGE          *
 *                                                              *
 * Problem Statement                                            *
 * Have the function SecondGreatLow(arr) take the array of      *
 * numbers stored in arr and return the second lowest and second*
 * greatest numbers, respectively, separated by a space.        *
 * For example: if arr contains [7, 7, 12, 98, 106] the output  *
 * should be 12 98. The array will not be empty and will contain*
 * at least 2 numbers. It can get tricky if there's just        *
 * two numbers!                                                 *
 *                                                              *
 * Examples                                                     *
 * Input 1: new int[] {1, 42, 42, 180}                          *
 * Output 1: 42 42                                              *
 *                                                              *
 * Input 2: new int[] {4, 90}                                   *
 * Output 2: 90 4                                               *
 *                                                              *
 ***************************************************************/"""
def secondgreatlow(arr):
    if len(arr) == 1 or len(arr) == 0:
        return 0
    elif len(arr) == 2:
        x,y = arr[1],arr[0]
        z = str(x) + ' ' + str(y)
        return z
    else:
        arr.sort()
        a = set(arr)
        b = sorted(a)
        if len(a) == 2:
            x,y = b[1],b[0]
            z = str(x) + ' ' + str(y)
            return z
        else:
            x,y = b[1],b[len(b)-2]
            z = str(x) + ' ' + str(y)
            return z
        
print(secondgreatlow([1, 42, 42, 180]))

"""/****************************************************************
 *             CODERBYTE RECTANGLE AREA CHALLENGE               *
 *                                                              *
 * Problem Statement                                            *
 * Have the function RectangleArea(strArr) take the array of    *
 * strings stored in strArr, which will only contain 4 elements *
 * and be in the form (x y) where x and y are both integers, and*
 * return the area of the rectangle formed by the 4 points on a *
 * Cartesian grid. The 4 elements will be in arbitrary order.   *
 * For example: strArr is ["(0 0)", "(3 0)", "(0 2)", "(3 2)"]  *
 * then your program should return 6 because the width of the   *
 * rectangle is 3 and the height is 2 and the area of a         *
 * rectangle is equal to the width * height.                    *
 *                                                              *
 * Examples                                                     *
 * Input 1: ["(1 1)","(1 3)","(3 1)","(3 3)"]                   *
 * Output 1: 4                                                  *
 *                                                              *
 * Input 2: ["(0 0)","(1 0)","(1 1)","(0 1)"]                   *
 * Output 2: 1                                                  *
 *                                                              *
 ***************************************************************/"""

def rectangulararea(arr):
    coordinates = [(int(i.strip('()').split()[0]),int(i.strip('()').split()[1])) for i in arr]
    x_coordinate = [i[0] for i in coordinates]
    y_coordinate = [i[1] for i in coordinates]
    
    width = max(x_coordinate) - min(x_coordinate)
    length = max(y_coordinate) - min(y_coordinate)
    return abs(width*length)
    
rectangulararea(["(0 0)","(1 0)","(1 1)","(0 1)"])

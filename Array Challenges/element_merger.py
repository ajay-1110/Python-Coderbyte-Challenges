"""/****************************************************************
 *              CODERBYTE ELEMENT MERGER CHALLENGE              *
 *                                                              *
 * Problem Statement                                            *
 * Have the function ElementMerger(arr) take the array of       *
 * positive integers stored in arr and perform the following    *
 * algorithm: continuously get the difference of adjacent       *
 * integers to create a new array of integers, then do the same *
 * for the new array until a single number is left and return   *
 * that number.                                                 *
 *                                                              *
 * For example: if arr is [4, 5, 1, 2, 7] then taking the       *
 * difference of each pair of elements produces the following   *
 * new array: [1, 4, 1, 5]. Then do the same for this new array *
 * to produce [3, 3, 4] -> [0, 1] -> 1. So for this example your*
 * program should return the number 1 because that is what's    *
 * left at the end.                                             *
 *                                                              *
 * Examples                                                     *
 * Input 1: [5, 7, 16, 1, 2]                                    *
 * Output 1: 7                                                  *
 *                                                              *
 * Input 2: [1, 1, 1, 2]                                        *
 * Output 2: 1                                                  *
 *                                                              *
 ***************************************************************/
"""

def elementmerger(arr):
    x = len(arr)
    while x >= 1:
        for i in range(1,x):
            a = abs(arr[i] - arr[i-1])
            arr.append(a)
        arr = arr[x:]
        x = len(arr)
        if x == 1:
            break
    return arr[0]

print(elementmerger([5, 7, 16, 1, 2]))

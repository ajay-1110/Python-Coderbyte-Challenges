"""/****************************************************************
 *              CODERBYTE ARRAY SIMILAR CHALLENGE               *
 *                                                              *
 * Problem Statement                                            *
 * Two arrays are called similar if one can be obtained from    *
 * another by swapping at most one pair of elements in one of   *
 * the arrays. Given two arrays a and b, check whether they are *
 * similar.                                                     *
 *                                                              *
 * Examples                                                     *
 * Input 1: a = [1, 2, 3] and b = [1, 2, 3]                     *
 * Output 1: true                                               *
 *                                                              *
 * Input 2: [1, 2, 3] and b = [2, 1, 3]                         *
 * Output 2: true                                               *
 * Explanation: We can obtain b from a by swapping 2 and 1 in b.*
 *                                                              *
 * Input 3: [1, 2, 2] and b = [2, 1, 1]                         *
 * Output 3: false                                              *
 * Explanation: Any swap of any two elements either in a or b   * 
 * won't make a and b equal                                     *
 *                                                              *
 ***************************************************************/"""

def similararr(a,b):
    if len(a)!=len(b):
        return False
    diff = []
    for i in range(len(a)):
        if a[i] != b[i]:
            diff.append(i)
            
    if len(diff) == 0 or len(diff) == 2:
        return [sorted(a[i] for i in diff)] == [sorted(b[i] for i in diff)]
    return False

print(similararr([1, 2, 3,4],[2, 1, 3,4]))

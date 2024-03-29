"""/****************************************************************
 *          CODERBYTE NEAREST SMALLER VALUES CHALLENGE		*
 *                                                              *
 * Problem Statement                                            *
 * Have the function NearestSmallerValues(arr) take the array of*
 * integers stored in arr, and for each element in the list,    *
 * search all the previous values for the nearest element that  *
 * is smaller than (or equal to) the current element and create *
 * a new list from these numbers. If there is no element before *
 * a certain position that is smaller, input a -1.              *
 * For example: if arr is [5, 2, 8, 3, 9, 12] then the nearest  *
 * smaller values list is [-1, -1, 2, 2, 3, 9].                 *
 * The logic is as follows: For 5, there is no smaller previous *
 * value so the list so far is [-1]. For 2, there is also no    *
 * smaller previous value, so the list is now [-1, -1].         *
 * For 8, the nearest smaller value is 2 so the list is now     *
 * [-1, -1, 2]. For 3, the nearest smaller value is also 2,     *
 * so the list is now [-1, -1, 2, 2]. This goes on to produce   *
 * the answer above. Your program should take this final list   *
 * and return the elements as a string separated by a           *
 * space: -1 -1 2 2 3 9                                         *
 *                                                              *
 * Examples                                                     *
 * Input 1: [5, 3, 1, 9, 7, 3, 4, 1]                            *
 * Output 1: -1 -1 -1 1 1 1 3 1                                 *
 *                                                              *
 * Input 2: [2, 4, 5, 1, 7]                                     *
 * Output 2: -1 2 4 -1 1                                        *
 *                                                              *
 ***************************************************************/"""
def nearestsmallvalue(arr):
    a = [-1]
    for i in range(1,len(arr)):
        if any(arr[j] <= arr[i] for j in range(i)):
            x = max(j for j in range(i) if arr[j]<= arr[i])
            a.append(arr[x])
        else:
            a.append(-1)
    return "".join(str(i)+' ' for i in a)[:-1]

print(nearestsmallvalue([5, 3, 1, 9, 7, 3, 4, 1]))

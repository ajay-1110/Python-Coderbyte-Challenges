"""/****************************************************************
 *                CODERBYTE LRU CACHE CHALLENGE                 *
 *                                                              *
 * Problem Statement                                            *
 * Have the function LRUCache( strArr ) take the array of       *
 * characters stored in strArr, which will contain characters   *
 * ranging from A to Z in some arbitrary order, and determine   *
 * what elements still remain in a virtual cache that can hold  *
 * up to 5 elements with an LRU cache algorithm implemented.    *
 *                                                              *
 * For example: if strArr is ["A","B","C","D","A","E","D","Z"], *
 * then the following steps are taken:                          *
 *                                                              *
 * 1) "A" doesn't exist in the cache, so store it in the cache  *
 * 2) "B" doesn't exist in the cache, so store it in the cache  *
 * So far the cache contains: ["A", "B"].                       *
 * 3) "C" doesn't exist in the cache, so store it in the cache  *
 * 4) "D" doesn't exist in the cache, so store it in the cache  *
 * So far the cache contains: ["A", "B", "C", "D"].             *
 * 5) Now A is accessed again, but it exists in th cache already*
 * so it is brought to the front: ["B", "C", "D", "A"].         *
 * 6) "E" doesn't exist in the cache, so store it in the cache  *
 * So far the cache contains: ["B", "C", "D", "A", "E"].        *
 * 7) D is accessed again so its brought to the front as follows*
 * So far the cache contains: ["B", "C", "A", "E", "D"].        *
 * 8) Z does not exist in the cache so add it to the front &    *
 * remove the least recently used element                       *
 * So far the cache contains: ["C", "A", "E", "D", "Z"].        *
 *                                                              *
 * Now the caching steps have been completed and your program   *
 * should return the order of the cache with the elements joined*
 * into a string, separated by a hyphen. Therefore, for the     *
 * example above your program should return C-A-E-D-Z.          *
 *                                                              *
 * Examples                                                     *
 * Input 1: ["A", "B", "A", "C", "A", "B"]                      *
 * Output 1: C-A-B                                              *
 *                                                              *
 * Input 2: ["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]       *
 * Output 2: E-D-Q-Z-C                                          *
 *                                                              *
 ***************************************************************/"""

def lrucache(strarr):
    cache = []
    for i in strarr:
        if i in cache:
            cache.remove(i)
            cache.append(i)
        else:
            if len(cache) == 5:
                cache.pop(0)
            cache.append(i)
    x =  "".join(i+'-' for i in cache)
    return x[:len(x)-1]

print(lrucache(["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]))
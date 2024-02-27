"""/****************************************************************
 *             CODERBYTE COUNTING ANAGRAMS CHALLENGE            *
 *                                                              *
 * Problem Statement                                            *
 * Have the function CountingAnagrams(str) take the str         *
 * parameter & determine how many anagrams exist in the string. *
 * An anagram is a new word that is produced from rearranging   *
 * the characters in a different word.                          *
 * For example: cars and arcs are anagrams.                     *
 *                                                              *
 * Your program should determine how many anagrams exist in a   *
 * given string and return the total number.                    *
 *                                                              *
 * For example: "cars are very cool so are arcs and my os"      *
 * then your program should return 2 because "cars" and "arcs"  *
 * form 1 anagram and "so" and "os" form a 2nd anagram.         *
 *                                                              *
 * The word "are" occurs twice in the string but it isn't an    *
 * anagram because it is the same word just repeated.           *
 * The string will contain only spaces and lowercase letters,   *
 * no punctuation, numbers, or uppercase letters.               *
 *                                                              *
 * Examples                                                     *
 * Input 1: "aa aa odg dog gdo"                                 *
 * Output 1: 2                                                  *
 *                                                              *
 * Input 2: "a c b c run urn urn"                               *
 * Output 2: 1                                                  *
 *                                                              *
 ***************************************************************/"""
from collections import Counter
def anagram5(arr):
    x = arr.strip().split()
    y = list(set(x))
    new = []
    for i in y:
        a = "".join(j for j in sorted(i))
        new.append(a)
    y = Counter(new)
    count = 0
    for value in y.values():
        if value >= 2:
            count += value - 1
    return count

print(anagram5("a c b c run urn urn"))

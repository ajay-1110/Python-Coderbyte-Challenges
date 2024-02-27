""" * Problem Statement                                            *
 * Have the function PalindromicSubstring(str) take the str     *
 * parameter being passed and find the longest palindromic      *
 * substring, which means the longest substring which is read   *
 * the same forwards as it is backwards.                        *
 * For example: if str is "abracecars" then your program should *
 * return the string racecar because it is the longest          *
 * palindrome within the input string.                          *
 *                                                              *
 * The input will only contain lowercase alphabetic characters. *
 * The longest palindromic substring will always be unique,     *
 * but if there is none that is longer than 2 characters,       *
 * return the string none.                                      *
 *                                                              *
 * Examples                                                     *
 * Input 1: "hellosannasmith"                                   *
 * Output 1: sannas                                             *
 *                                                              *
 * Input 2: "abcdefgg"                                          *
 * Output 2: none                                               *
 *                                                              *
 ***************************************************************/"""

def PalindromicSubstring(s):
    longest_palindrome = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
                
    if len(longest_palindrome) <= 2:
        return "none"
    return longest_palindrome

# Test cases
print(PalindromicSubstring("hellosannasmith")) 
print(PalindromicSubstring("abracecars"))        
